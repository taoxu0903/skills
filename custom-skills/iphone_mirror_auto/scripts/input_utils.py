"""Mouse click and coordinate conversion utilities."""

import subprocess
import time


# iPhone Mirroring requires the window to be frontmost for clicks to register.
IPHONE_MIRROR_ACTIVATE_CMD = [
    "osascript", "-e",
    'tell application "iPhone镜像" to activate'
]
IPHONE_MIRROR_ACTIVATE_CMD_EN = [
    "osascript", "-e",
    'tell application "iPhone Mirroring" to activate'
]


def _ensure_frontmost():
    """Bring iPhone Mirroring window to the front before clicking."""
    result = subprocess.run(IPHONE_MIRROR_ACTIVATE_CMD, capture_output=True)
    if result.returncode != 0:
        subprocess.run(IPHONE_MIRROR_ACTIVATE_CMD_EN, capture_output=True)
    time.sleep(0.5)


def ocr_bbox_to_screen(bbox, image_size, window_position, retina_scale=2, shadow_offset=(0, 0)):
    """Convert Apple Vision OCR bounding box to screen coordinates.

    Apple Vision returns normalized coords (0~1) with origin at bottom-left.
    This converts to macOS screen coordinates suitable for cliclick.

    The screenshot may include window shadow (from screencapture -l without -o).
    shadow_offset specifies the pixel padding on each side so that coordinates
    are mapped to the actual window content, not the shadow.

    Args:
        bbox: Dict with bbox_x, bbox_y, bbox_w, bbox_h (normalized 0~1).
        image_size: Tuple (pixel_width, pixel_height) of the screenshot.
        window_position: Tuple (window_x, window_y) in screen coords.
        retina_scale: Display scale factor (2 for Retina).
        shadow_offset: Tuple (shadow_x, shadow_y) pixel offset from shadow.

    Returns:
        Tuple (screen_x, screen_y) — center of the bounding box in screen coords.
    """
    img_w, img_h = image_size
    win_x, win_y = window_position
    shad_x, shad_y = shadow_offset

    # Normalized → pixel coords (flip Y: bottom-left origin → top-left origin)
    px_x = bbox["bbox_x"] * img_w
    px_y = (1.0 - bbox["bbox_y"] - bbox["bbox_h"]) * img_h
    px_w = bbox["bbox_w"] * img_w
    px_h = bbox["bbox_h"] * img_h

    # Center of bounding box in pixels
    center_px_x = px_x + px_w / 2
    center_px_y = px_y + px_h / 2

    # Subtract shadow to get content-relative pixel coords, then scale
    screen_x = int(win_x + (center_px_x - shad_x) / retina_scale)
    screen_y = int(win_y + (center_px_y - shad_y) / retina_scale)

    return screen_x, screen_y


def click(x, y, delay_after=0.5):
    """Click at screen coordinates using cliclick.

    Ensures iPhone Mirroring is the frontmost window before clicking,
    since it only responds to clicks when it has focus.

    Args:
        x, y: Screen coordinates.
        delay_after: Seconds to wait after clicking.
    """
    _ensure_frontmost()
    result = subprocess.run(
        ["cliclick", f"c:{x},{y}"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"cliclick failed: {result.stderr}")
    if delay_after > 0:
        time.sleep(delay_after)


def click_ocr_target(bbox, image_size, window_position, retina_scale=2, delay_after=0.5, shadow_offset=(0, 0)):
    """Click on an OCR-detected text region.

    Args:
        bbox: OCR result dict with bbox_x/y/w/h.
        image_size: Screenshot pixel dimensions.
        window_position: Window screen position.
        retina_scale: Display scale factor.
        delay_after: Wait time after click.
        shadow_offset: Pixel offset from window shadow.

    Returns:
        Tuple (screen_x, screen_y) that was clicked.
    """
    sx, sy = ocr_bbox_to_screen(bbox, image_size, window_position, retina_scale, shadow_offset)
    click(sx, sy, delay_after)
    return sx, sy


def notify(title, message):
    """Show a macOS notification.

    Args:
        title: Notification title.
        message: Notification body text.
    """
    subprocess.run(
        [
            "osascript",
            "-e",
            f'display notification "{message}" with title "{title}" sound name "Default"',
        ],
        capture_output=True,
    )


def swipe_up(x, y, distance=200, duration_ms=500):
    """Perform a swipe-up gesture (for scrolling) using cliclick drag.

    Args:
        x, y: Starting screen coordinates.
        distance: Pixels to swipe up.
        duration_ms: Duration of the swipe.
    """
    end_y = y - distance
    # cliclick drag: dd = drag down (press), du = drag up (release)
    subprocess.run(
        ["cliclick", f"dd:{x},{y}", f"du:{x},{end_y}"],
        capture_output=True,
        text=True,
    )
    time.sleep(0.5)
