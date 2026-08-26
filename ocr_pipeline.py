"""
Regional Sign Board Translator — OCR + Dictionary Translation Pipeline

Reads a sign board image, extracts text using Tesseract OCR (English +
Tamil), then attempts to translate recognized lines using a curated
signage dictionary.

Usage:
    python3 ocr_pipeline.py <image_path>
    python3 ocr_pipeline.py --test   (runs on all bundled sample images)
"""
import sys
import os
import pytesseract
from PIL import Image
from translator import translate_line

TEST_IMAGES_DIR = "test_images"


def extract_text(image_path: str) -> str:
    """Runs Tesseract OCR using both English and Tamil trained models."""
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="eng+tam")
    return text


def process_image(image_path: str):
    print(f"\n{'='*60}")
    print(f"Processing: {image_path}")
    print(f"{'='*60}")

    raw_text = extract_text(image_path)
    lines = [l for l in raw_text.splitlines() if l.strip()]

    if not lines:
        print("No text detected.")
        return

    for line in lines:
        translation = translate_line(line)
        print(f"  Detected : {line.strip()}")
        print(f"  Translated: {translation}")
        print("  " + "-" * 40)


def run_test_suite():
    if not os.path.isdir(TEST_IMAGES_DIR):
        print(f"Test images directory '{TEST_IMAGES_DIR}' not found. "
              f"Run generate_test_images.py first.")
        return

    images = sorted(os.listdir(TEST_IMAGES_DIR))
    if not images:
        print("No test images found.")
        return

    print(f"Running OCR pipeline on {len(images)} test images...\n")
    for fname in images:
        process_image(os.path.join(TEST_IMAGES_DIR, fname))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 ocr_pipeline.py <image_path> | --test")
        sys.exit(1)

    if sys.argv[1] == "--test":
        run_test_suite()
    else:
        process_image(sys.argv[1])
