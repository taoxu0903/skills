"""Screen capture and window management for iPhone Mirroring."""

import subprocess
import tempfile
import os
import Quartz
from PIL import Image


# The process name is "iPhone镜像" (Chinese) on Chinese macOS
IPHONE_MIRROR_PROCESS_NAMES = ["iPhone镜像", "iPhone Mirroring"]


def find_iphone_mirror_window():
    """Find the iPhone Mirroring content window.

    Returns:
        Dict with keys: window_id, x, y, width, height.
        Returns the main content window (phone-shaped, typically ~354x781 logical).

    Raises:
        RuntimeError if iPhone Mirroring window not found.
    """
    windows = Quartz.CGWindowListCopyWindowInfo(
        Quartz.kCGWindowListOptionAll, Quartz.kCGNullWindowID
    )

    candidates = []
    for w in windows:
        owner = w.get("kCGWindowOwnerName", "")
        if owner not in IPHONE_MIRROR_PROCESS_NAMES:
            continue
        bounds = w.get("kCGWindowBounds", {})
        height = bounds.get("Height", 0)
        width = bounds.get("Width", 0)
        # Filter out menu bar items (33px height) and outer frame windows
        # The phone content window is tall & narrow (aspect ratio ~0.45)
        if height > 400 and width > 200 and width < height:
            candidates.append({
                "window_id": w.get("kCGWindowNumber"),
                "x": bounds["X"],
                "y": bounds["Y"],
                "width": width,
                "height": height,
            })

    if not candidates:
        raise RuntimeError(
            "iPhone Mirroring window not found. "
            "Ensure iPhone Mirroring is open and the phone screen is visible."
        )

    # Pick the tallest candidate (most likely the actual phone content)
    candidates.sort(key=lambda c: c["height"], reverse=True)
    return candidates[0]


def capture_window(window_id=None, output_path=None, win_info=None):
    """Capture a screenshot of the iPhone Mirroring window.

    Uses -o -l (by window ID, no shadow). The image size matches
    window_size * retina_scale exactly, so coordinate conversion
    is straightforward: pixel / retina + window_origin = screen_coord.

    Args:
        window_id: CGWindowNumber. If None, uses win_info or auto-detects.
        output_path: Where to save the PNG. If None, uses a temp file.
        win_info: Window info dict. If None, auto-detects. Updated with
            shadow_x, shadow_y fields.

    Returns:
        Tuple of (image_path, image_width, image_height) in pixels.
    """
    if win_info is None:
        win_info = find_iphone_mirror_window()
    if window_id is None:
        window_id = win_info["window_id"]

    if output_path is None:
        fd, output_path = tempfile.mkstemp(suffix=".png", prefix="iphone_mirror_")
        os.close(fd)

    result = subprocess.run(
        ["screencapture", "-x", "-o", "-l", str(window_id), output_path],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"screencapture failed: {result.stderr}")

    img = Image.open(output_path)
    img_w, img_h = img.size

    # With -o flag, the screenshot has no window shadow.
    # The image size should match window_size * retina exactly.
    # Store zero shadow offsets for backward compatibility.
    win_info["shadow_x"] = 0
    win_info["shadow_y"] = 0

    return output_path, img_w, img_h


def get_retina_scale():
    """Detect Retina display scale factor.

    Returns:
        2 for Retina displays, 1 for non-Retina.
    """
    main_display = Quartz.CGMainDisplayID()
    mode = Quartz.CGDisplayCopyDisplayMode(main_display)
    pixel_width = Quartz.CGDisplayModeGetPixelWidth(mode)
    logical_width = Quartz.CGDisplayModeGetWidth(mode)
    if logical_width > 0:
        return pixel_width / logical_width
    return 2  # safe default for Apple Silicon Macs
