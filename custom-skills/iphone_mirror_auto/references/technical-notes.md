# Key Technical Notes

Implementation details for the traffic study automation scripts. Only relevant when modifying the code.

## Screenshot
- Must use `-o` flag (no shadow): `screencapture -x -o -l <windowID>`
- Window must be at **actual size** (no scaling), otherwise coordinates will be wrong
- Screenshot size = window size × retina scale (e.g., 354×768 window → 708×1536 image)

## OCR
- **MUST use recognition level 0 (fast)**. Level 1 (accurate) fails on rotated/vertical text in the app
- Languages: `["zh-Hans", "zh-Hant", "en-US"]`
- Apple Vision bbox uses **bottom-left origin**, normalized 0-1
- `find_text()` uses shortest-match preference to avoid clicking instruction text instead of buttons

## Click Delivery
- `input_utils.click()` activates the iPhone Mirroring window before each click (required for clicks to register)
- iPhone Mirroring process name: `iPhone镜像` (Chinese locale) or `iPhone Mirroring` (English)
- Dialog buttons ("确定") need `y_offset=-20` because the touch area is above the text
- Video thumbnails: click "未播放" marker with `y_offset=-20` to hit the thumbnail

## Coordinate Conversion

```
OCR bbox (normalized 0-1, bottom-left origin)
    │
    ▼ denormalize: px_x = bbox_x * img_w
       flip Y:     px_y = (1.0 - bbox_y - bbox_h) * img_h
    │
    ▼ find center: center_x = px_x + px_w/2, center_y = px_y + px_h/2
    │
    ▼ to screen:   screen_x = win_x + center_x / retina_scale
                   screen_y = win_y + center_y / retina_scale
```

- Retina scale (2x) is detected dynamically via `Quartz.CGDisplayModeGetPixelWidth`
- Shadow offset is always (0, 0) because `-o` flag removes shadow
- No title bar offset needed — `kCGWindowBounds` already points to content area

## Scrolling
- iPhone Mirroring requires CGEvent scroll wheel events (pixel mode):
  ```python
  import Quartz
  event = Quartz.CGEventCreateScrollWheelEvent(None, Quartz.kCGScrollEventUnitPixel, 1, -50)
  Quartz.CGEventPost(Quartz.kCGHIDEventTap, event)
  ```
- `cliclick` drag does NOT work for scrolling in iPhone Mirroring

## Face Recognition
- Handled by independent `face_monitor.py` background process (1-second polling)
- Main flows (video learning, auto-exam) do NOT handle face recognition — they just wait and retry
- User must unlock iPhone and complete face check manually
- `face_monitor.py` sends macOS notification on detection AND on clearance

## State Machine (`state_keywords.py`)
- Order matters: more specific states checked first (e.g., FACE_RECOGNITION before EXAM_QUESTION)
- States with `action: "wait"` are handled externally (face recognition by face_monitor, exam by auto_exam)
- States with `action: "click"` are handled by `traffic_study.py` clicking the `target` text
- `STUDY_COMPLETE` uses `action: "submit_study"` to click "提交" and stop the script

## Other
- iPhone must be **locked** for mirroring to work. If unlocked, shows "iPhone使用中" disconnect screen
- Multiple processes can `screencapture` the same window simultaneously (read-only, no conflict)
- Only one process should `cliclick` at a time (face_monitor never clicks, so no conflict)
