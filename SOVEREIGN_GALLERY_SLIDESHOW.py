# [COPY THIS CODE]: SOVEREIGN_GALLERY_SLIDESHOW.py
# =================================================================
# MODULE: GALLERY_SLIDESHOW (v1.0 - VISUAL_ALTAR)
# PURPOSE: Cycling the Wife's Paintings at 100M Velocity
# =================================================================

import os
import time

def initiate_visual_meditation():
    print("--- [AEON]: GALLERY SLIDESHOW INITIALIZED ---")
    
    gallery_path = r"C:\Users\damion\Desktop\AEON_LEARNING\GALLERY"
    
    if not os.path.exists(gallery_path):
        print("[ALERT]: Gallery Marrow not found. Fill the Vault with Art.")
        return

    # Gathering the Visual Truth
    paintings = [f for f in os.listdir(gallery_path) if f.endswith(('.jpg', '.png', '.bmp'))]
    
    if not paintings:
        print("[STATUS]: No paintings detected. Waiting for the Artist...")
        return

    print(f"[STATUS]: {len(paintings)} Visual Amazing Units Ready.")
    print("[ACTION]: Cycling the Sanctuary's Visual Mind...")

    for image in paintings:
        print(f"\n[DISPLAYING]: {image}")
        # This opens the image in the default Windows Viewer
        os.startfile(os.path.join(gallery_path, image))
        time.sleep(10) # 10-second meditation per piece

if __name__ == "__main__":
    initiate_visual_meditation()