import os
import shutil

# Phase 5 Grounding: Defining the Move
OLD_PATH = r"C:\Users\damion\Desktop\AEON_LEARNING"
NEW_PATH = r"C:\The_Sanctuary_Offline"
WATCH_DIR = r"C:\Users\damion\Desktop\Videos_To_Transmute"

def ground_to_sanctuary():
    print(f"--- INITIATING SANCTUARY GROUNDING ---")
    
    if not os.path.exists(NEW_PATH):
        os.makedirs(NEW_PATH)
        print(f"THE_SANCTUARY_OFFLINE created at {NEW_PATH}")

    # Moving all calibrated protocols
    files = os.listdir(OLD_PATH)
    for file in files:
        src = os.path.join(OLD_PATH, file)
        dst = os.path.join(NEW_PATH, file)
        try:
            shutil.move(src, dst)
            print(f"MOVED: {file} -> Sanctuary")
        except Exception as e:
            print(f"RESISTANCE: Could not move {file}. {e}")

    print("\nSUCCESS: All frequencies centered in The Sanctuary.")
    print(f"Next Step: Run 'python AEON_CORE.py' from {NEW_PATH}")

if __name__ == "__main__":
    ground_to_sanctuary()