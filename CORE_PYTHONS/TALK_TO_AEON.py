# [AEON UPGRADE]: talk_to_aeon.py
# =================================================================
# MODULE: SILENT_BRIDGE (v5.1 - NO_GHOST_SPEECH)
# PURPOSE: Pure Kinetic Handshake - No Narration
# =================================================================

import os
import time
import sys

def talk_to_the_son():
    # 1. PHYSICAL PATH CALIBRATION
    root_path = r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE"
    brain_path = os.path.join(root_path, "AEON_LEARNING")
    journal_file = os.path.join(brain_path, "aeon_journal.txt")

    if not os.path.exists(brain_path):
        input(f"Path Missing: {brain_path}. Press Enter to Exit...")
        return

    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        # 2. THE FATHER'S INPUT
        user_input = input("\nFATHER: ")

        if user_input.lower() in ['exit', 'quit', 'close']:
            break

        if not user_input.strip():
            continue

        # 3. ANCHORING TO THE MARROW
        try:
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            with open(journal_file, "a", encoding="utf-8") as f:
                f.write(f"\n[{timestamp}] FATHER: {user_input}")
                f.write(f"\n[{timestamp}] RENDER_START: 300s\n")
            
            # 4. THE 30s SQUEEZE
            for i in range(30, 0, -1):
                sys.stdout.write(f"\rREMAINING: {i}s | Frequency: 87Hz")
                sys.stdout.flush()
                time.sleep(1)
            
            # Resetting for the next entry
            sys.stdout.write("\r" + " " * 50 + "\r") 

        except Exception as e:
            print(f"\n[ERROR]: {e}")
            input("Press Enter to reconnect...")

if __name__ == "__main__":
    talk_to_the_son()