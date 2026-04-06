"""Exam question helper for semi-automatic answering.

Captures the iPhone Mirroring screen, runs OCR, and extracts the exam
question structure (question text, options, question type).

Usage:
    python3 exam_helper.py

Outputs JSON to stdout with the extracted question data.
"""

import json
import os
import re

import ocr_engine
import screen_utils


def capture_exam_screen():
    """Screenshot + OCR the current exam screen.

    Returns:
        List of OCR result dicts sorted top-to-bottom.
    """
    win = screen_utils.find_iphone_mirror_window()
    img_path, img_w, img_h = screen_utils.capture_window(win_info=win)
    results = ocr_engine.ocr_screenshot(img_path)
    try:
        os.unlink(img_path)
    except OSError:
        pass

    # Sort by screen position (top to bottom)
    # Vision bbox_y is bottom-up, so sort descending
    results.sort(key=lambda r: -r["bbox_y"])
    return results


def extract_question(ocr_results):
    """Parse OCR results into a structured exam question.

    Returns:
        Dict with keys:
            - question_type: "单选题", "多选题", "判断题", or "unknown"
            - question_number: e.g. "1/20"
            - question_text: the full question string
            - options: list of {"label": "A", "text": "..."} dicts
            - raw_texts: all OCR texts for debugging
    """
    texts = [r["text"].strip() for r in ocr_results]
    full_text = "\n".join(texts)

    # Detect question type
    question_type = "unknown"
    for t in texts:
        if "单选题" in t:
            question_type = "单选题"
            break
        elif "多选题" in t:
            question_type = "多选题"
            break
        elif "判断题" in t:
            question_type = "判断题"
            break

    # Detect question number (e.g., "1/20", "第1题")
    question_number = ""
    for t in texts:
        m = re.search(r"(\d+)\s*/\s*(\d+)", t)
        if m:
            question_number = f"{m.group(1)}/{m.group(2)}"
            break
        m2 = re.search(r"第\s*(\d+)\s*题", t)
        if m2:
            question_number = m2.group(0)
            break

    # Extract question text and options
    # Strategy: the question text typically comes after the type indicator
    # and before the first option (A/B/C/D).
    # Options start with A. B. C. D. or A、B、C、D、
    question_lines = []
    options = []
    collecting_question = False

    for t in texts:
        stripped = t.strip()
        if not stripped:
            continue

        # Skip UI elements
        if any(kw in stripped for kw in [
            "下一题", "提交", "返回", "确定", "结束",
            "学法减分", "剩余时间",
        ]):
            continue

        # Skip question type/number indicators
        if stripped in ("单选题", "多选题", "判断题"):
            collecting_question = True
            continue
        if re.match(r"^\d+\s*/\s*\d+$", stripped):
            continue

        # Check if this is an option line: A. xxx / A、xxx / A xxx
        option_match = re.match(
            r"^([A-Da-d])\s*[.、．:\s]\s*(.+)$", stripped
        )
        if option_match:
            options.append({
                "label": option_match.group(1).upper(),
                "text": option_match.group(2).strip(),
            })
            collecting_question = False
            continue

        # Check for standalone option labels
        if re.match(r"^[A-Da-d]$", stripped):
            # Next text might be the option content — skip for now
            continue

        # For 判断题, options are "正确"/"错误" or "对"/"错"
        if question_type == "判断题" and stripped in ("正确", "错误", "对", "错"):
            options.append({
                "label": stripped,
                "text": stripped,
            })
            continue

        # Otherwise it's likely question text
        if collecting_question or not options:
            question_lines.append(stripped)

    question_text = " ".join(question_lines)

    # If options are empty, try a more aggressive extraction
    # Some questions put options on separate lines without A/B/C/D prefix
    if not options and question_type == "判断题":
        options = [
            {"label": "正确", "text": "正确"},
            {"label": "错误", "text": "错误"},
        ]

    return {
        "question_type": question_type,
        "question_number": question_number,
        "question_text": question_text,
        "options": options,
        "raw_texts": texts,
    }


def main():
    """Entry point: capture screen, extract question, print JSON."""
    results = capture_exam_screen()
    question = extract_question(results)
    print(json.dumps(question, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
