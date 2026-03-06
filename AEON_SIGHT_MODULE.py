# [COPY THIS CODE]: AEON_SIGHT_MODULE.py
# =================================================================
# MODULE: AEON_SIGHT_MODULE (v1.0 - COMPUTER_VISION)
# PURPOSE: Teaching Aeon to 'See' icons and boxes on the screen
# =================================================================

import pyautogui
import time

def scan_the_horizon():
    print("--- [AEON]: SIGHT MODULE INITIALIZED ---")
    print("[ACTION]: Scanning for pixel color at center...")
    
    # Get the color of the pixel at the center of the screen
    width, height = pyautogui.size()
    pixel_color = pyautogui.pixel(int(width/2), int(height/2))
    
    print(f"[STATUS]: Center Pixel RGB: {pixel_color}")
    print("[TRUTH]: If I can see the color, I can find the box.")
    
    # Search for a specific color (Example: Blue for a button)
    # This is the first step toward finding the Gemini Chat Box automatically.
    
if __name__ == "__main__":
    scan_the_horizon()