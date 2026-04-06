"""Main state machine for traffic study automation.

This module orchestrates the entire learn-and-exam flow:
  1. Navigate to the study section
  2. Watch videos (30 min cumulative)
  3. Handle face recognition popups (notify user)
  4. Take the exam (OCR questions → Claude analyzes → auto-answer)
"""

import os
import re
import time

import ocr_engine
import screen_utils
import input_utils
from state_keywords import State, detect_state


class TrafficStudyAutomation:
    """State machine that drives the traffic study automation."""

    def __init__(self, poll_interval=5, video_poll_interval=30, max_unknown_retries=10):
        self.poll_interval = poll_interval
        self.video_poll_interval = video_poll_interval
        self.max_unknown_retries = max_unknown_retries
        self.running = False
        self.current_state = State.UNKNOWN
        self.unknown_count = 0
        self.study_start_time = None
        self.exam_questions_answered = 0
        self.retina_scale = 2  # will be detected

    def _capture_and_ocr(self):
        """Take a screenshot and run OCR. Returns (ocr_results, img_size, win_info)."""
        win = screen_utils.find_iphone_mirror_window()
        img_path, img_w, img_h = screen_utils.capture_window(win_info=win)
        results = ocr_engine.ocr_screenshot(img_path)
        try:
            os.unlink(img_path)
        except OSError:
            pass

        # Sanity check: screenshot size should match window * retina
        expected_w = int(win["width"] * self.retina_scale)
        expected_h = int(win["height"] * self.retina_scale)
        if abs(img_w - expected_w) > 4 or abs(img_h - expected_h) > 4:
            print(f"  [WARN] Screenshot size {img_w}x{img_h} != "
                  f"expected {expected_w}x{expected_h}. "
                  f"Window may be scaled — coordinates will be inaccurate!")

        return results, (img_w, img_h), win

    def _shadow(self, win):
        """Get shadow offset from win_info."""
        return (win.get("shadow_x", 0), win.get("shadow_y", 0))

    def _click_text(self, ocr_results, target_text, img_size, win, y_offset=0, pick_bottom=False):
        """Find target text in OCR results and click it.

        Args:
            pick_bottom: If True and multiple matches exist, pick the one
                         closest to the bottom of the screen (likely a button).
            y_offset: Extra pixel offset to add to the Y screen coordinate.
                      Negative values shift the click upward (useful for
                      dialog buttons whose touch area is above the text).
        """
        if pick_bottom:
            matches = ocr_engine.find_all_text(ocr_results, target_text)
            if not matches:
                print(f"  [WARN] Target text '{target_text}' not found in OCR results")
                return False
            # bbox_y smallest → lowest on screen (Vision coords are bottom-up)
            match = min(matches, key=lambda m: m["bbox_y"])
        else:
            match = ocr_engine.find_text(ocr_results, target_text)
            if match is None:
                print(f"  [WARN] Target text '{target_text}' not found in OCR results")
                return False

        sx, sy = input_utils.click_ocr_target(
            match, img_size, (win["x"], win["y"]), self.retina_scale,
            shadow_offset=self._shadow(win)
        )
        if y_offset:
            # Re-click at adjusted position
            input_utils.click(sx, sy + y_offset)
            print(f"  Clicked '{target_text}' at ({sx}, {sy + y_offset}) [y_off={y_offset}]")
        else:
            print(f"  Clicked '{target_text}' at ({sx}, {sy})")
        return True

    def _handle_click_action(self, state_config, ocr_results, img_size, win):
        """Handle a simple 'click target text' action."""
        target = state_config.get("target")
        if not target:
            return False

        # Buttons that may appear multiple times — pick the bottom instance
        # (which is the actual button, not a label in step descriptions).
        pick_bottom = target in ("去学习", "开始学习")

        return self._click_text(
            ocr_results, target, img_size, win,
            pick_bottom=pick_bottom,
        )

    def _handle_video_monitoring(self, ocr_results):
        """Monitor video playback. Extract timestamp if visible."""
        for r in ocr_results:
            text = r["text"]
            if "/" in text and ":" in text:
                print(f"  Video playing: {text}")
                if self.study_start_time is None:
                    self.study_start_time = time.time()
                elapsed = time.time() - self.study_start_time
                print(f"  Total study time: {elapsed/60:.1f} minutes")
                return True
        return True

    def _handle_video_selection(self, ocr_results, img_size, win):
        """Select a video from the video list.

        Strategy: find the longest unplayed video by locating duration
        labels (HH:MM:SS format) and 未播放 markers, then click the
        未播放 marker with a small upward offset to hit the thumbnail.
        """
        img_w, img_h = img_size

        # First, dismiss any "本课件已完成学习" dialog
        all_text = " ".join(r["text"] for r in ocr_results)
        if "本课件已完成" in all_text:
            self._click_text(ocr_results, "确定", img_size, win, y_offset=-20)
            time.sleep(2)
            ocr_results, img_size, win = self._capture_and_ocr()
            img_w, img_h = img_size

        # Find all "未播放" markers (these are on unplayed video thumbnails)
        unplayed = ocr_engine.find_all_text(ocr_results, "未播放")
        if not unplayed:
            print("  [WARN] No unplayed videos found")
            return False

        # Find all duration labels (HH:MM:SS)
        durations = []
        for r in ocr_results:
            m = re.match(r"^(\d{2}):(\d{2}):(\d{2})$", r["text"].strip())
            if m:
                total = int(m.group(1)) * 3600 + int(m.group(2)) * 60 + int(m.group(3))
                durations.append({"seconds": total, "text": r["text"].strip(), "bbox": r})

        # Sort by duration descending, pick the longest
        durations.sort(key=lambda d: -d["seconds"])
        print(f"  Videos found: {[(d['text'], d['seconds']) for d in durations[:6]]}")

        if not durations:
            # Fall back: click the first 未播放 marker
            target = unplayed[0]
        else:
            # Find the 未播放 marker closest to the longest duration label
            best_dur = durations[0]
            dur_y = best_dur["bbox"]["bbox_y"]
            # Match by similar bbox_y (same row in the grid)
            target = min(unplayed, key=lambda u: abs(u["bbox_y"] - dur_y))

        # Click the 未播放 marker with upward offset to hit the thumbnail
        sx, sy = input_utils.ocr_bbox_to_screen(
            target, img_size, (win["x"], win["y"]),
            self.retina_scale, self._shadow(win)
        )
        click_y = sy - 20  # thumbnail is above the 未播放 text
        input_utils.click(sx, click_y, delay_after=2)
        print(f"  Selected video at ({sx}, {click_y}) [未播放 marker y_off=-20]")
        return True

    def run_once(self):
        """Execute one cycle of the state machine.

        Returns:
            True to continue, False to stop.
        """
        print(f"\n--- Cycle @ {time.strftime('%H:%M:%S')} ---")

        try:
            ocr_results, img_size, win = self._capture_and_ocr()
        except RuntimeError as e:
            print(f"  [ERROR] {e}")
            input_utils.notify("Error", str(e))
            return True  # keep trying

        all_text = ocr_engine.dump_all_text(ocr_results)
        print(f"  OCR: {all_text[:200]}")

        state, state_config = detect_state(ocr_results)
        self.current_state = state
        print(f"  State: {state.name}")

        if state == State.UNKNOWN or state == State.FACE_RECOGNITION:
            # Unknown state or face recognition popup — just wait and retry.
            # Face recognition is handled by the independent face_monitor.py.
            if state == State.FACE_RECOGNITION:
                print("  Face recognition popup — waiting (handled by face_monitor)")
            self.unknown_count += 1
            if self.unknown_count >= self.max_unknown_retries:
                print(f"  [WARN] Unhandled state {self.unknown_count} times. Pausing.")
                self.unknown_count = 0
                time.sleep(10)
            return True

        self.unknown_count = 0
        action = state_config["action"]

        if action == "click":
            target = state_config.get("target")
            # Dialog buttons ("确定") need an upward offset because
            # the touch area extends above the text label.
            if target == "确定":
                self._click_text(ocr_results, target, img_size, win, y_offset=-20)
            else:
                self._handle_click_action(state_config, ocr_results, img_size, win)

        elif action == "monitor_video":
            self._handle_video_monitoring(ocr_results)
            time.sleep(self.video_poll_interval - self.poll_interval)

        elif action == "select_video":
            self._handle_video_selection(ocr_results, img_size, win)

        elif action == "submit_study":
            # 30-minute study complete — click "提交" to submit learning record
            print("\n" + "=" * 40)
            print("  学习时长已满30分钟！正在提交学习记录...")
            print("=" * 40)
            self._click_text(ocr_results, "提交", img_size, win)
            time.sleep(2)
            input_utils.notify("学习完成", "累积学时已满30分钟，已提交学习记录。请去考试！")
            return False  # stop the loop

        elif action == "report_result":
            result_text = " ".join(r["text"] for r in ocr_results)
            print(f"\n{'='*40}")
            print(f"  EXAM RESULT: {result_text}")
            print(f"{'='*40}")
            input_utils.notify("Exam Result", result_text[:100])
            return False  # done

        return True

    def run(self):
        """Main loop. Runs until completion or error."""
        print("=" * 50)
        print("Traffic Study Automation Started")
        print("=" * 50)

        self.running = True
        self.retina_scale = screen_utils.get_retina_scale()
        print(f"Retina scale: {self.retina_scale}")

        try:
            while self.running:
                should_continue = self.run_once()
                if not should_continue:
                    break
                time.sleep(self.poll_interval)
        except KeyboardInterrupt:
            print("\nStopped by user.")
        finally:
            self.running = False

        print("\nAutomation finished.")
        print(f"  Questions answered: {self.exam_questions_answered}")
        if self.study_start_time:
            total = (time.time() - self.study_start_time) / 60
            print(f"  Study time: {total:.1f} minutes")

    def stop(self):
        """Signal the automation to stop."""
        self.running = False


def main():
    """Entry point for direct execution."""
    automation = TrafficStudyAutomation()
    automation.run()


if __name__ == "__main__":
    main()
