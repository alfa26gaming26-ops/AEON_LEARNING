# =================================================================
# MODULE: AEON_AUTO_EVOLVE (v1.1 - THE BUILDER)
# PURPOSE: Automatically creates .py files from your clipboard
# =================================================================

import os
import pyperclip # If this fails, run: pip install pyperclip
import time

class SovereignBuilder:
    def __init__(self):
        # HARD-CODED ABSOLUTE PATH to prevent "Ghosting"
        self.save_path = r"C:\Users\damion\Desktop\AEON_LEARNING"
        
        # Ensure the folder actually exists before writing
        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)

    def forge_file(self, file_name):
        print(f"--- [AEON]: AUTO-EVOLVE INITIALIZED ---")
        print(f"[STATUS]: Searching clipboard for Truth...")
        
        # 1. Grab whatever you just "Copied" from our chat
        content = pyperclip.paste()
        
        # 2. Basic check to make sure it's actually Python code
        if "import" in content or "def" in content or "class" in content:
            target_file = os.path.join(self.save_path, file_name)
            
            try:
                with open(target_file, "w") as f:
                    f.write(content)
                
                print(f"\n[SUCCESS]: {file_name} has been FORGED.")
                print(f"[LOCATION]: {target_file}")
                print("-" * 40)
            except Exception as e:
                print(f"[!] BUILD ERROR: {e}")
        else:
            print("\n[ALERT]: Clipboard does not contain valid Python code.")
            print("[ACTION]: Copy the code block from the chat and try again.")

if __name__ == "__main__":
    # We will name the NEXT file you copy 'AEON_NEXT_STEP.py'
    # Change the name below for each new script we build
    target = "AEON_NEXT_STEP.py"
    
    Builder = SovereignBuilder()
    Builder.forge_file(target)
    
    # Keeps window open so you can see the Success message
    input("\n[LOCKED]: Press ENTER to close the Forge...")