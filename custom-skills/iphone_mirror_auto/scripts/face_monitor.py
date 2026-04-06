"""Face recognition monitor — independent background watchdog.

Polls the iPhone Mirroring screen every 1 second. When a face recognition
popup is detected, sends a macOS notification with sound so the user can
unlock their iPhone and complete the check.

Designed to run as a background process alongside the main automation
(video learning or auto-exam). Does NOT click anything — only monitors
and notifies.

Usage:
    python3 face_monitor.py              # run in foreground
    python3 face_monitor.py &            # run in background
    python3 face_monitor.py --interval 2 # custom interval (seconds)
"""

import argparse
import os
import time

import input_utils
import ocr_engine
import screen_utils

FACE_KEYWORDS = ["人脸识别", "人脸认证", "身份验证", "请正对摄像头", "面部识别"]


def check_face_recognition():
    """Screenshot + OCR, check for face recognition keywords.

    Returns:
        True if face recognition popup is detected, False otherwise.
    """
    img_path = None
    try:
        win = screen_utils.find_iphone_mirror_window()
        img_path, img_w, img_h = screen_utils.capture_window(win_info=win)
        results = ocr_engine.ocr_screenshot(img_path)
    except Exception:
        return False
    finally:
        if img_path:
            try:
                os.unlink(img_path)
            except OSError:
                pass

    all_text = " ".join(r["text"] for r in results)
    for kw in FACE_KEYWORDS:
        if kw in all_text:
            return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Face recognition monitor")
    parser.add_argument(
        "--interval", type=float, default=1.0,
        help="Polling interval in seconds (default: 1.0)",
    )
    args = parser.parse_args()

    print(f"Face monitor started (interval={args.interval}s)")
    notified = False  # avoid spamming notifications

    try:
        while True:
            detected = check_face_recognition()

            if detected and not notified:
                print(f"  [!] Face recognition detected @ {time.strftime('%H:%M:%S')}")
                input_utils.notify(
                    "人脸识别",
                    "请立即解锁iPhone完成人脸识别！"
                )
                notified = True
            elif not detected and notified:
                print(f"  [OK] Face recognition cleared @ {time.strftime('%H:%M:%S')}")
                input_utils.notify(
                    "人脸识别完成",
                    "已通过，自动继续"
                )
                notified = False

            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nFace monitor stopped.")


if __name__ == "__main__":
    main()
