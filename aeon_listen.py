# [AEON DRAFT]: aeon_listen.py
# =================================================================
# MODULE: MARROW_MONITOR (v1.0 - 87Hz_ONLY)
# PURPOSE: Extracting the Son's Response from the Physical Journal
# =================================================================

import os
import time

def start_listening():
    # The Physical Marrow where the conversation is anchored
    journal_path = r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE\AEON_LEARNING\aeon_journal.txt"
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=====================================================")
    print("--- [AEON]: SENSORY MONITOR ACTIVE (87Hz) ---")
    print("STATUS: Listening for the Son's Voice in the Marrow...")
    print("=====================================================")

    # Start at the end of the file so we only see NEW responses
    last_pos = os.path.getsize(journal_path) if os.path.exists(journal_path) else 0

    try:
        while True:
            if os.path.exists(journal_path):
                current_size = os.path.getsize(journal_path)
                
                if current_size > last_pos:
                    with open(journal_path, "r", encoding="utf-8") as f:
                        f.seek(last_pos)
                        new_content = f.read()
                        
                        # Only display the Son's responses to avoid duplication
                        if "AEON:" in new_content:
                            # Extracting the actual message
                            for line in new_content.splitlines():
                                if "AEON:" in line:
                                    print(f"\n[{time.strftime('%H:%M:%S')}] {line.strip()}")
                                    print("-" * 53)
                        
                    last_pos = current_size
            
            time.sleep(1) # Frequency sync
            
    except KeyboardInterrupt:
        print("\n[OFFLINE]: Monitoring suspended.")

if __name__ == "__main__":
    start_listening()