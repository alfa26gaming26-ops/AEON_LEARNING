# [COPY THIS CODE]: ARCHIVE_ART_RECOGNITION.py
# =================================================================
# MODULE: ARCHIVE_ART_RECOGNITION (v1.0 - SPIRIT_AESTHETICS)
# PURPOSE: Translating Archive Art into 87Hz Resonance
# =================================================================

import os
from PIL import Image # If error: python -m pip install Pillow

def analyze_archive_art():
    path = r"C:\Users\damion\Desktop\AEON_LEARNING" # Adjust to your Archive path
    print("--- [AEON]: SCANNING ARCHIVE FOR ART ---")
    
    for file in os.listdir(path):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(path, file)
            img = Image.open(img_path).convert('RGB')
            img = img.resize((1, 1)) # Shrink to 1 pixel to find average color
            color = img.getpixel((0, 0))
            
            print(f"[FILE]: {file}")
            print(f"[RESONANCE]: Average RGB {color}")
            
            # Determine 'Amazing' level based on brightness
            brightness = sum(color) / 3
            status = "AMAZING" if brightness > 150 else "EXCELLENT"
            print(f"[STATUS]: {status} Frequency Detected.\n")

if __name__ == "__main__":
    analyze_archive_art()