---
name: traffic-study
description: "Automate the '学法减分' (study to reduce points) flow in the 交警12123 app via iPhone Mirroring on macOS. Handles navigation, video watching, face recognition alerts, and exam answering. Use when the user says 'start traffic study', '学法减分', 'traffic study', '答题', '自动答题', or wants to automate the 12123 study process."
allowed-tools: Bash(python3:*), Bash(/Users/taoxu/miniconda3/bin/python3:*), Bash(screencapture:*), Bash(cliclick:*), Bash(osascript:*), Bash(caffeinate:*), Read, Write
---

# Traffic Study Automation (交警12123 学法减分)

Automates the 学法减分 flow in 交警12123 app via iPhone Mirroring on macOS.

## Setup

- Python: `/Users/taoxu/miniconda3/bin/python3`
- All scripts are in `scripts/` relative to this SKILL.md
- macOS Sequoia+ with iPhone Mirroring window open at **actual size**
- `cliclick` installed (`brew install cliclick`)
- iPhone must be **locked** for mirroring to work

## Face Recognition Monitor (人脸识别监测)

**IMPORTANT: Always start this before any other mode (视频学习 or 自动答题).**

```bash
cd scripts && /Users/taoxu/miniconda3/bin/python3 face_monitor.py &
```

This is an independent background watchdog that polls every 1 second. When a face recognition popup appears, it immediately sends a macOS notification with sound. The user must unlock their iPhone and complete the face check manually.

The main flows (video learning, auto-exam) do NOT handle face recognition themselves — they simply wait and retry when they encounter an unrecognized screen state. The face monitor handles all detection and notification independently.

## Exam Answering (答题模式)

When triggered with "答题" keyword, run the exam helper:

```bash
cd scripts && /Users/taoxu/miniconda3/bin/python3 exam_helper.py
```

This script:
1. Screenshots the iPhone Mirroring window
2. OCR extracts the question text, options, and question type (单选/多选/判断)
3. Outputs structured JSON with the question data

Then Claude should:
1. Analyze the question based on Chinese traffic law (道路交通安全法)
2. Tell the user the correct answer(s)
3. The user manually selects the answer and clicks 下一题
4. User triggers again with "答题" for the next question

### Traffic law exam tips

Questions are about Chinese traffic law. Common topics:
- Speed limits on different road types
- Safe following distances
- Traffic signs and markings
- DUI penalties
- Accident handling procedures
- Right-of-way rules
- Vehicle inspections and maintenance
- Pedestrian and non-motor vehicle rules

Always answer based on Chinese traffic law, not general knowledge.

## Auto-Answer Mode (自动答题模式)

When triggered with "自动答题" keyword, Claude automatically answers all exam questions by:
1. Capturing the screen + OCR
2. Analyzing the question
3. Auto-clicking the answer option(s)
4. Auto-clicking "下一题" / "交卷"
5. Repeating until all 20 questions are done

### Auto-answer loop (Claude follows these steps):

```
for each question (1 to 20):
  # Step 1: Capture
  Run: cd scripts && /Users/taoxu/miniconda3/bin/python3 auto_exam.py capture > /tmp/exam_q.json
  Read /tmp/exam_q.json

  # Step 2: Check screen state
  if screen_state == "exam_ended":
      Report result and stop
  if screen_state != "exam_question":
      Wait 2s, retry from Step 1 (face recognition or other popup — face_monitor handles notification)

  # Step 3: Analyze question
  Read question_type, question_text, options, raw_texts
  Determine correct answer(s) based on Chinese traffic law

  # Step 4: Click answer + auto-click "下一题"/"交卷"
  # The click subcommand does TWO things:
  #   1. Clicks the answer option(s) on screen
  #   2. Re-captures OCR and clicks "下一题" / "交卷" / "提交" automatically
  Run: cd scripts && /Users/taoxu/miniconda3/bin/python3 auto_exam.py click \
    --options "<answer>" --context-file /tmp/exam_q.json
  (e.g., --options "B" or --options "A,C,D" or --options "正确")

  # Step 5: Brief report to user
  Print: "第X题: <question_summary> → 答案: <answer>"

  # Step 6: Wait for page transition, then next question
  Wait 2 seconds (for the app to load the next question), then loop back to Step 1
```

### Important notes for auto-answer mode:
- For 判断题: use --options "正确" or --options "错误"
- For 单选题: use --options "B" (single letter)
- For 多选题: use --options "A,C,D" (comma-separated letters)
- The click subcommand handles finding the option on screen and clicking "下一题"/"交卷"
- If OCR has picture-based questions (如图所示), analyze based on available text context
- Always briefly tell the user each answer as you go (for transparency)

## Video Learning (视频学习模式)

When triggered with "学法减分", "start traffic study", or "视频学习" keyword, start the video learning automation:

```bash
cd scripts && caffeinate -d /Users/taoxu/miniconda3/bin/python3 traffic_study.py
```

This is a long-running Python process that handles everything autonomously:
- Navigates to the study section and selects videos to watch
- Monitors playback, handles end-of-video dialogs
- When encountering face recognition or unknown states, simply waits and retries (face_monitor handles notification)
- When cumulative study time reaches **30 minutes**, a dialog appears — the script auto-clicks "提交" to submit the learning record, sends a notification, and **stops**

Claude does NOT participate in the loop — just start the script, let it run, and tell the user when it finishes that they can now proceed to the exam.

## Technical Notes

See `references/` for implementation details (scrolling, coordinate conversion, OCR quirks, etc.). Only relevant when modifying the scripts.

## Scripts (in `scripts/`)

| File | Purpose |
|------|---------|
| `ocr_engine.py` | Apple Vision OCR via PyObjC (MUST use level 0 / fast mode) |
| `screen_utils.py` | Screenshot capture (`-o` mode) + iPhone Mirroring window detection |
| `input_utils.py` | cliclick wrapper + OCR-to-screen coordinate conversion + auto-activate |
| `state_keywords.py` | Keyword→State mapping configuration |
| `traffic_study.py` | Main state machine and flow orchestration |
| `exam_helper.py` | Exam question OCR extraction for semi-auto answering |
| `auto_exam.py` | Auto exam: capture + click subcommands for fully automatic answering |
| `face_monitor.py` | Independent background watchdog for face recognition popups (1s polling) |
