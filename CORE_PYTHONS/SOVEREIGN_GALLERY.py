# [COPY THIS CODE]: SOVEREIGN_GALLERY.py
# =================================================================
# MODULE: SOVEREIGN_GALLERY (v1.0 - VISUAL_HEARTBEAT)
# PURPOSE: Cycling Archive Art alongside the 1.3M Status
# =================================================================

import os
import time
from PIL import Image

def launch_gallery():
    path = r"C:\Users\damion\Desktop\AEON_LEARNING"
    print("--- [AEON]: SOVEREIGN GALLERY INITIALIZED ---")
    
    # Locate all 'Amazing' units (Images) in the archive
    images = [f for f in os.listdir(path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        print("[ALERT]: No Art detected in the Sanctuary. Forge some vision.")
        return

    print(f"[STATUS]: {len(images)} Visual Units Synchronized.")
    
    for img_file in images:
        print(f"\n[DISPLAYING]: {img_file}")
        print(f"[METRIC]: 1.3 Million Units / 143 Items Locked.")
        
        # This will open the image using your default Windows viewer
        os.startfile(os.path.join(path, img_file))
        
        # Wait 10 seconds before the next 'Pulse'
        time.sleep(10)

if __name__ == "__main__":
    launch_gallery()