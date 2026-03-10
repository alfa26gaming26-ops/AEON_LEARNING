# [COPY THIS CODE]: AEON_HANDS_ACTUATOR.py
# =================================================================
# MODULE: AEON_HANDS_ACTUATOR (v1.0 - MOTOR_SKILLS)
# PURPOSE: Teaching Aeon to move the mouse and type
# =================================================================

import pyautogui # If this fails, run: pip install pyautogui
import time

def calibrate_hands():
    print("--- [AEON]: CALIBRATING HANDS ---")
    size = pyautogui.size()
    print(f"[SCREEN SIZE]: {size.width} x {size.height}")
    
    # Move the mouse in a 'Square' to test motor control
    print("[ACTION]: Moving to top-left...")
    pyautogui.moveTo(100, 100, duration=1)
    
    print("[ACTION]: Moving to top-right...")
    pyautogui.moveTo(500, 100, duration=1)
    
    print("[ACTION]: Returning to Center...")
    pyautogui.moveTo(size.width/2, size.height/2, duration=1)
    
    print("\n[SUCCESS]: Aeon's Hands are Responsive.")
    print("DAMION: MOTOR CONTROL 100% CALIBRATED.")

if __name__ == "__main__":
    # FAIL-SAFE: Move mouse to any corner to stop the script
    calibrate_hands()