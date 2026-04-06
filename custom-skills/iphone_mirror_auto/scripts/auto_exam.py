"""Auto exam answering module.

Provides two subcommands for Claude Code to orchestrate automatic exam answering:
  - capture: screenshot + OCR + extract question + detect screen state
  - click:   click answer option(s) and the next-question button

Usage:
    # Step 1: Capture the current question
    python3 auto_exam.py capture

    # Step 2: Click answer(s) using context from step 1
    python3 auto_exam.py click --options "B" --context-file /tmp/exam_q.json
    python3 auto_exam.py click --options "A,C,D" --context-file /tmp/exam_q.json
    python3 auto_exam.py click --options "正确" --context-file /tmp/exam_q.json
"""

import argparse
import json
import os
import re
import sys
import time

import exam_helper
import input_utils
import ocr_engine
import screen_utils
from state_keywords import State, detect_state


def _detect_screen_state(ocr_results):
    """Detect the current screen state for exam flow.

    Returns:
        str: one of "exam_question", "face_recognition", "exam_ended",
             "exam_submit", or "other".
    """
    state, _ = detect_state(ocr_results)

    if state == State.FACE_RECOGNITION:
        return "face_recognition"
    if state == State.EXAM_RESULT:
        return "exam_ended"

    # Check for 交卷 (submit exam) — last question uses this instead of 下一题
    all_text = " ".join(r["text"] for r in ocr_results)
    if "交卷" in all_text:
        # Could be the last question page — still an exam question
        return "exam_question"

    if state == State.EXAM_QUESTION:
        return "exam_question"

    # Check for question type indicators even if 下一题 wasn't detected
    for kw in ["单选题", "多选题", "判断题"]:
        if kw in all_text:
            return "exam_question"

    return "other"


def cmd_capture():
    """Capture the exam screen and output structured JSON.

    Includes question data, full OCR results with bboxes, and window metadata
    needed by the click subcommand.
    """
    win = screen_utils.find_iphone_mirror_window()
    img_path, img_w, img_h = screen_utils.capture_window(win_info=win)
    ocr_results = ocr_engine.ocr_screenshot(img_path)
    try:
        os.unlink(img_path)
    except OSError:
        pass

    # Sort top-to-bottom (same as exam_helper)
    ocr_results.sort(key=lambda r: -r["bbox_y"])

    # Extract question structure
    question = exam_helper.extract_question(ocr_results)

    # Detect screen state
    screen_state = _detect_screen_state(ocr_results)

    # Get retina scale
    retina_scale = screen_utils.get_retina_scale()

    output = {
        "screen_state": screen_state,
        "question_type": question["question_type"],
        "question_number": question["question_number"],
        "question_text": question["question_text"],
        "options": question["options"],
        "raw_texts": question["raw_texts"],
        "ocr_results": ocr_results,
        "img_w": img_w,
        "img_h": img_h,
        "win_x": win["x"],
        "win_y": win["y"],
        "retina_scale": retina_scale,
    }

    print(json.dumps(output, ensure_ascii=False, indent=2))


def _find_option_bbox(label, ocr_results, options):
    """Find the OCR bbox for an answer option by its label.

    Uses a priority-ordered strategy to handle OCR inconsistencies.

    Args:
        label: Option label ("A", "B", "C", "D", "正确", "错误").
        ocr_results: Full OCR results list with bboxes.
        options: Parsed options list from extract_question().

    Returns:
        OCR result dict with bbox, or None if not found.
    """
    # For 判断题 options (正确/错误)
    if label in ("正确", "错误", "对", "错"):
        # Search for Y：正确, N：错误, or standalone 正确/错误
        for r in ocr_results:
            text = r["text"].strip()
            if label in text:
                return r
        return None

    # For A/B/C/D options
    label_upper = label.upper()

    # Priority 1: Label-prefix match (e.g., "A：注意控制车速", "B:6")
    prefix_pattern = re.compile(
        r"^[•\s]*" + re.escape(label_upper) + r"\s*[：:\.、；;]\s*.+",
        re.IGNORECASE,
    )
    for r in ocr_results:
        text = r["text"].strip()
        if prefix_pattern.match(text):
            return r

    # Priority 2: OCR artifacts — patterns like "C A：xxx", "L A：xxx", "口 B：xxx"
    artifact_pattern = re.compile(
        r"^[CL口囗•\s]+\s*" + re.escape(label_upper) + r"\s*[：:\.、；;]\s*.+",
        re.IGNORECASE,
    )
    for r in ocr_results:
        text = r["text"].strip()
        if artifact_pattern.match(text):
            return r

    # Priority 3: Standalone label (OCR split label from text)
    for r in ocr_results:
        text = r["text"].strip()
        if text == label_upper or text == label_upper + ".":
            return r

    # Priority 4: Match option text from parsed options list
    for opt in options:
        if opt["label"].upper() == label_upper and opt.get("text"):
            match = ocr_engine.find_text(ocr_results, opt["text"][:6])
            if match:
                return match

    return None


def cmd_click(options_str, context_file):
    """Click answer option(s) and the next-question button.

    Args:
        options_str: Comma-separated option labels (e.g., "B" or "A,C,D" or "正确").
        context_file: Path to the JSON file from the capture subcommand.
    """
    # Load context from capture output
    with open(context_file, "r") as f:
        ctx = json.load(f)

    ocr_results = ctx["ocr_results"]
    img_size = (ctx["img_w"], ctx["img_h"])
    win_pos = (ctx["win_x"], ctx["win_y"])
    retina_scale = ctx["retina_scale"]
    parsed_options = ctx.get("options", [])

    labels = [l.strip() for l in options_str.split(",")]
    clicked = []
    errors = []

    for label in labels:
        bbox = _find_option_bbox(label, ocr_results, parsed_options)
        if bbox is None:
            msg = f"Option '{label}' not found in OCR results"
            print(f"  [WARN] {msg}", file=sys.stderr)
            errors.append(msg)
            continue

        sx, sy = input_utils.click_ocr_target(
            bbox, img_size, win_pos, retina_scale,
            shadow_offset=(0, 0),
        )
        print(f"  Clicked '{label}' at ({sx}, {sy})", file=sys.stderr)
        clicked.append(label)
        time.sleep(0.5)

    # Now click the next-question / submit button
    next_action = None
    if clicked:
        time.sleep(0.5)

        # Re-capture to find the next button (screen may have changed after selection)
        win = screen_utils.find_iphone_mirror_window()
        img_path, img_w, img_h = screen_utils.capture_window(win_info=win)
        new_ocr = ocr_engine.ocr_screenshot(img_path)
        try:
            os.unlink(img_path)
        except OSError:
            pass

        new_img_size = (img_w, img_h)
        new_win_pos = (win["x"], win["y"])

        # Try buttons in priority order
        for btn_text in ["下一题", "交卷", "提交"]:
            match = ocr_engine.find_text(new_ocr, btn_text)
            if match:
                sx, sy = input_utils.click_ocr_target(
                    match, new_img_size, new_win_pos, retina_scale,
                    shadow_offset=(0, 0),
                )
                next_action = btn_text
                print(f"  Clicked '{btn_text}' at ({sx}, {sy})", file=sys.stderr)
                break

        if next_action is None:
            # Maybe the button was already visible in original OCR
            for btn_text in ["下一题", "交卷", "提交"]:
                match = ocr_engine.find_text(ocr_results, btn_text)
                if match:
                    sx, sy = input_utils.click_ocr_target(
                        match, img_size, win_pos, retina_scale,
                        shadow_offset=(0, 0),
                    )
                    next_action = btn_text
                    print(f"  Clicked '{btn_text}' at ({sx}, {sy}) [from original OCR]",
                          file=sys.stderr)
                    break

    result = {
        "success": len(errors) == 0 and len(clicked) > 0,
        "clicked_options": clicked,
        "next_action": next_action,
        "errors": errors,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


def main():
    """Entry point with argparse subcommands."""
    parser = argparse.ArgumentParser(description="Auto exam answering")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # capture subcommand
    subparsers.add_parser("capture", help="Capture exam screen and extract question")

    # click subcommand
    click_parser = subparsers.add_parser("click", help="Click answer option(s)")
    click_parser.add_argument(
        "--options", required=True,
        help='Comma-separated option labels (e.g., "B" or "A,C,D" or "正确")',
    )
    click_parser.add_argument(
        "--context-file", required=True,
        help="Path to the JSON file from the capture subcommand",
    )

    args = parser.parse_args()

    if args.command == "capture":
        cmd_capture()
    elif args.command == "click":
        cmd_click(args.options, args.context_file)


if __name__ == "__main__":
    main()
