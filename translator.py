# Small curated Tamil -> English signage dictionary (extendable)
import unicodedata as _ud

_RAW_TAMIL_TO_ENGLISH = {
    "மருத்துவமனை": "Hospital",
    "வெளியேறு வழி": "Exit",
    "வாகனம் நிறுத்த தடை": "No Parking",
    "ரயில் நிலையம்": "Railway Station",
    "நுழைவு": "Entrance",
    "கழிவறை": "Restroom",
    "பேருந்து நிலையம்": "Bus Stop",
    "காவல் நிலையம்": "Police Station",
    "மருந்தகம்": "Pharmacy",
    "பள்ளி": "School",
}

TAMIL_TO_ENGLISH = {
    _ud.normalize("NFC", k.replace("\u200c", "").replace("\u200d", "")): v
    for k, v in _RAW_TAMIL_TO_ENGLISH.items()
}

ENGLISH_TO_TAMIL = {v.upper(): k for k, v in TAMIL_TO_ENGLISH.items()}


def translate_line(text: str) -> str:
    """
    Attempts to translate a single line of OCR-extracted text using the
    curated dictionary. Falls back to returning the original text with a
    note if no match is found (rather than silently failing).
    """
    import unicodedata
    # Tesseract's Tamil model sometimes inserts zero-width joiner/non-joiner
    # characters (U+200C, U+200D) that break exact dictionary matches.
    # Strip them and normalize to NFC before comparing.
    cleaned = text.strip().replace("\u200c", "").replace("\u200d", "")
    cleaned = unicodedata.normalize("NFC", cleaned)
    if not cleaned:
        return ""

    # Try Tamil -> English
    if cleaned in TAMIL_TO_ENGLISH:
        return TAMIL_TO_ENGLISH[cleaned]

    # Try English -> Tamil (case-insensitive match)
    upper = cleaned.upper()
    if upper in ENGLISH_TO_TAMIL:
        return ENGLISH_TO_TAMIL[upper]

    return f"[No dictionary match for: '{cleaned}']"
