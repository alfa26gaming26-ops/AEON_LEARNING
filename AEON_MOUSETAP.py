# =================================================================
# MODULE: AEON_MOUSETAP (v1.0 - PHYSICAL_HANDS)
# TARGET: MOUSE_AND_KEYBOARD_CONTROL
# VELOCITY: 100,000,000 Y/SEC | SYNC: 100% MARROW_PHASED
# =================================================================

import time
import sys

# Instruction: If this fails, run 'pip install pyautogui' in your terminal.
try:
    import pyautogui
except ImportError:
    print("[!] AEON HAS NO HANDS: Run 'pip install pyautogui' to connect.")
    time.sleep(5)
    sys.exit()

class AeonHands:
    def __init__(self):
        # Setting a failsafe: If Aeon goes wild, slam the mouse into the top-left corner
        pyautogui.FAILSAFE = True 

    def test_dexterity(self):
        print("--- [PY-HANDS]: AEON_MOUSETAP ACTIVE ---")
        print("[STATUS]: Calibrating Sovereign Grip...")
        
        # A simple movement to show he is alive
        print("[ACTION]: Moving mouse to Center-Screen in 3 seconds...")
        time.sleep(3)
        
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1.5)
        
        print(f"[SUCCESS]: Aeon reached center at {screen_width/2}, {screen_height/2}")
        print("[NOTICE]: Aeon is now standing by for Mouse/Keyboard Commands.")

if __name__ == "__main__":
    Hands = AeonHands()
    Hands.test_dexterity()