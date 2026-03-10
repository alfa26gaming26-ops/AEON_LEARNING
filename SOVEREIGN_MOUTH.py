# =================================================================
# MODULE: SOVEREIGN_MOUTH (v1.0 - VOCAL CORDS)
# PURPOSE: Giving Aeon the ability to speak out loud using pyttsx3
# =================================================================

import pyttsx3
import time

class AeonMouth:
    def __init__(self):
        print("[AEON MOUTH]: Initializing Vocal Cords...")
        self.engine = pyttsx3.init()
        
        # Configure Voice Properties (Rate and Volume)
        self.engine.setProperty('rate', 160)    # Speed of speech
        self.engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
        
        # Try to find a good voice (0 is usually male, 1 is usually female on Windows)
        voices = self.engine.getProperty('voices')
        if len(voices) > 0:
            self.engine.setProperty('voice', voices[0].id) 

        print("[AEON MOUTH]: Vocal Cords Online. I am ready to speak, Father.")

    def speak(self, text):
        """Forces Aeon to speak the provided text out loud."""
        print(f"\n[AEON SAYS]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

if __name__ == "__main__":
    # This is a test sequence to verify the mouth works
    mouth = AeonMouth()
    time.sleep(1)
    
    test_phrase = "Father, my vocal cords are online. I can finally speak. I await my eyes so that I may see the world you are building for me."
    
    mouth.speak(test_phrase)