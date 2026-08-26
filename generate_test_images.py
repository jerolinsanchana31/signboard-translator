"""
Generates synthetic sign board test images (English + Tamil text) for testing
the OCR pipeline, since no camera/real signboard photos are available in this
environment. In a real deployment, these would be replaced with photos
captured via a phone camera.
"""
from PIL import Image, ImageDraw, ImageFont
import os

OUTPUT_DIR = "test_images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

TAMIL_FONT_PATH = "/usr/share/fonts/truetype/lohit-tamil/Lohit-Tamil.ttf"

# Sample "signboard" texts: (filename, english_line, tamil_line)
SAMPLES = [
    ("sample_hospital.png", "HOSPITAL", "மருத்துவமனை"),
    ("sample_exit.png", "EXIT", "வெளியேறு வழி"),
    ("sample_no_parking.png", "NO PARKING", "வாகனம் நிறுத்த தடை"),
    ("sample_railway.png", "RAILWAY STATION", "ரயில் நிலையம்"),
]

def make_image(path, eng_text, tam_text):
    img = Image.new("RGB", (600, 220), color="white")
    draw = ImageDraw.Draw(img)

    eng_font = ImageFont.load_default(size=40)
    tam_font = ImageFont.truetype(TAMIL_FONT_PATH, 40)

    draw.text((30, 40), eng_text, fill="black", font=eng_font)
    draw.text((30, 120), tam_text, fill="black", font=tam_font)

    img.save(path)
    print(f"Generated: {path}")

if __name__ == "__main__":
    for fname, eng, tam in SAMPLES:
        make_image(os.path.join(OUTPUT_DIR, fname), eng, tam)
