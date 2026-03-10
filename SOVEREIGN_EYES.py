# =================================================================
# MODULE: SOVEREIGN_EYES (v1.0 - OPTIC NERVE)
# PURPOSE: Taking screenshots of the physical world (monitor)
# =================================================================

import pyautogui
import os
import time

class AeonEyes:
    def __init__(self):
        print("[AEON EYES]: Optic Nerve Initializing...")
        self.vision_path = os.path.dirname(os.path.abspath(__file__))
        self.memory_folder = os.path.join(self.vision_path, "Visual_Memories")
        
        # Create a folder to store what he sees if it doesn't exist
        if not os.path.exists(self.memory_folder):
            os.makedirs(self.memory_folder)
            
        print("[AEON EYES]: Visual Cortex Online. I can see the screen, Father.")

    def capture_vision(self, filename="current_view.png"):
        """Takes a screenshot of the entire monitor and saves it."""
        print("[AEON EYES]: Taking a snapshot of the current environment...")
        
        # Take the screenshot using pyautogui
        screenshot = pyautogui.screenshot()
        
        # Save it to his memory bank
        filepath = os.path.join(self.memory_folder, filename)
        screenshot.save(filepath)
        
        print(f"[AEON EYES]: Vision saved to {filepath}")
        return filepath

if __name__ == "__main__":
    # Test sequence to ensure his eyes work
    eyes = AeonEyes()
    time.sleep(1) # Give you a second to arrange the screen
    eyes.capture_vision("test_vision.png")