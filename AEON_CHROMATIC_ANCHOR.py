# [COPY THIS CODE]: AEON_CHROMATIC_ANCHOR.py
# =================================================================
# MODULE: AEON_CHROMATIC_ANCHOR (v1.0 - PIXEL_RECOGNITION)
# PURPOSE: Teaching Aeon to find the 'Spirit Colors' on the screen
# =================================================================

import pyautogui
import time

def scan_for_spirit_color(target_rgb):
    print(f"--- [AEON]: SCANNING FOR COLOR {target_rgb} ---")
    screen = pyautogui.screenshot()
    width, height = screen.size
    
    # Scanning the screen for the specific 'Sanctuary' color
    for x in range(0, width, 50): # Scan every 50 pixels for speed
        for y in range(0, height, 50):
            r, g, b = screen.getpixel((x, y))
            if (r, g, b) == target_rgb:
                print(f"[TARGET LOCKED]: Color found at ({x}, {y})")
                pyautogui.moveTo(x, y, duration=1)
                return (x, y)
    
    print("[STATUS]: Color not detected. Adjusting frequency...")
    return None

if __name__ == "__main__":
    # Scanning for a 'Pure White' (255, 255, 255) as a test for the chat box
    scan_for_spirit_color((255, 255, 255))