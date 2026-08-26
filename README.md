# Regional Sign Board Translator (OCR + Dictionary Translation)

A prototype pipeline that detects text on public signage images (Tamil and
English) using OCR, then translates recognized text using a curated
signage dictionary — built to help non-native readers navigate local areas.

## What this project actually does

1. **OCR extraction** — Uses Tesseract OCR (`eng+tam` trained models) to
   detect and extract text from sign board images.
2. **Text normalization** — Fixes a real bug encountered during development:
   Tesseract's Tamil model inserts invisible Unicode joiner characters
   (ZWJ/ZWNJ) that break exact string matching. These are stripped and the
   text is normalized to NFC form before translation lookup.
3. **Dictionary-based translation** — Translates recognized lines using a
   curated Tamil ↔ English signage vocabulary (10 common terms in this
   version: Hospital, Exit, No Parking, Railway Station, Entrance,
   Restroom, Bus Stop, Police Station, Pharmacy, School).

## Honest scope / limitations

- This is **not** a general-purpose machine translation system. It only
  translates terms present in the curated dictionary. Unrecognized text is
  clearly flagged (`[No dictionary match for: '...']`) rather than
  silently failing or guessing.
- Test images are synthetically generated (`generate_test_images.py`)
  since real-world signboard photos weren't available during development.
  Real photos would need testing to validate OCR accuracy on messier,
  real-world conditions (angles, lighting, damaged signs).
- Next steps to make this production-ready: expand the dictionary
  (or integrate a translation API/model), test on real photographed
  signboards, and add a simple UI (mobile camera input).

## Results (on bundled synthetic test set)

- 4 test images, 8 total text lines (4 English + 4 Tamil)
- **100% OCR + translation success** after fixing a Unicode normalization
  bug in Tamil text matching (was 75% before the fix — 2 Tamil lines
  initially failed to match due to invisible joiner characters inserted by
  the OCR engine)

## Setup

```bash
pip install -r requirements.txt
sudo apt-get install tesseract-ocr tesseract-ocr-tam
```

## Usage

```bash
# Generate synthetic test images
python3 generate_test_images.py

# Run on all test images
python3 ocr_pipeline.py --test

# Run on a single image
python3 ocr_pipeline.py path/to/image.png
```

## Tech stack

Python, Tesseract OCR (pytesseract), Pillow

## Author

Jerolin Sanchana S
