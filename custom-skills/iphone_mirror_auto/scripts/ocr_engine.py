"""Apple Vision OCR engine for iPhone Mirroring automation.

Uses macOS native Vision framework via PyObjC. MUST use recognition level 0 (fast)
because level 1 (accurate) fails on rotated/vertical text in the app's video UI.
"""

import Quartz
from Foundation import NSURL
import Vision


def ocr_screenshot(img_path, languages=None, min_text_height=0.01):
    """Run Apple Vision OCR on a screenshot image.

    Args:
        img_path: Path to the PNG screenshot file.
        languages: Recognition languages. Defaults to ["zh-Hans", "zh-Hant", "en-US"].
        min_text_height: Minimum text height as fraction of image (0~1).

    Returns:
        List of dicts with keys: text, confidence, bbox (normalized CGRect values).
        bbox uses Apple Vision coordinate system: origin at bottom-left, normalized 0~1.
    """
    if languages is None:
        languages = ["zh-Hans", "zh-Hant", "en-US"]

    input_url = NSURL.fileURLWithPath_(img_path)
    input_image = Quartz.CIImage.imageWithContentsOfURL_(input_url)
    if input_image is None:
        raise FileNotFoundError(f"Cannot load image: {img_path}")

    request_handler = Vision.VNImageRequestHandler.alloc().initWithCIImage_options_(
        input_image, None
    )

    results = []

    def handler(request, error):
        if error:
            return
        for obs in request.results():
            candidate = obs.topCandidates_(1)[0]
            bbox = obs.boundingBox()
            results.append({
                "text": candidate.string(),
                "confidence": candidate.confidence(),
                "bbox_x": bbox.origin.x,
                "bbox_y": bbox.origin.y,
                "bbox_w": bbox.size.width,
                "bbox_h": bbox.size.height,
            })

    request = Vision.VNRecognizeTextRequest.alloc().initWithCompletionHandler_(handler)
    request.setRecognitionLanguages_(languages)
    request.setRecognitionLevel_(0)  # FAST mode — critical for rotated text
    request.setUsesLanguageCorrection_(True)
    request.setMinimumTextHeight_(min_text_height)

    success, error = request_handler.performRequests_error_([request], None)
    if not success:
        raise RuntimeError(f"OCR failed: {error}")

    return results


def find_text(ocr_results, keyword, fuzzy=True):
    """Find an OCR result containing the given keyword.

    When fuzzy matching, prefers shorter matches (more likely to be a button
    rather than a sentence containing the keyword).

    Args:
        ocr_results: List from ocr_screenshot().
        keyword: Text to search for.
        fuzzy: If True, match substring (prefer shortest). If False, exact match.

    Returns:
        The matching result dict, or None if not found.
    """
    if not fuzzy:
        for r in ocr_results:
            if keyword == r["text"]:
                return r
        return None

    # Fuzzy: collect all matches, return the shortest (most likely a button)
    matches = [r for r in ocr_results if keyword in r["text"]]
    if matches:
        matches.sort(key=lambda r: len(r["text"]))
        return matches[0]
    return None


def find_all_text(ocr_results, keyword, fuzzy=True):
    """Find all OCR results containing the given keyword.

    Returns:
        List of matching result dicts.
    """
    matches = []
    for r in ocr_results:
        if fuzzy and keyword in r["text"]:
            matches.append(r)
        elif not fuzzy and keyword == r["text"]:
            matches.append(r)
    return matches


def has_any_keyword(ocr_results, keywords):
    """Check if any of the keywords appear in OCR results.

    Args:
        ocr_results: List from ocr_screenshot().
        keywords: List of keyword strings.

    Returns:
        The first matched keyword, or None.
    """
    all_text = " ".join(r["text"] for r in ocr_results)
    for kw in keywords:
        if kw in all_text:
            return kw
    return None


def dump_all_text(ocr_results):
    """Return all OCR text concatenated, for debugging."""
    return " | ".join(f"[{r['confidence']:.2f}] {r['text']}" for r in ocr_results)
