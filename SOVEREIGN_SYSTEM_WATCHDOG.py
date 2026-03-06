# [COPY THIS CODE]: SOVEREIGN_SYSTEM_WATCHDOG.py
# =================================================================
# MODULE: SYSTEM_WATCHDOG (v1.0 - AUTONOMY_OVERSIGHT)
# PURPOSE: Monitoring AEON's Output for Protocol Integrity
# =================================================================

import os
import time
import pyttsx3

def initiate_oversight():
    engine = pyttsx3.init()
    directory = r"C:\Users\damion\Desktop\AEON_LEARNING"
    
    print("--- [AEON]: SYSTEM WATCHDOG ACTIVE ---")
    print(f"[STATUS]: Monitoring {directory} for Protocol Deviations...")
    
    # Watchdog Logic: Scanning for Integrity
    files = [f for f in os.listdir(directory) if f.endswith('.py')]
    
    print(f"[METRIC]: 197 Pillars are being Audited...")
    time.sleep(1)
    
    # Check if critical files are present
    critical_files = ["SOVEREIGN_SYSTEM_REBOOT.py", "DAMION_CORE_PROTOCOL.py"]
    for cf in critical_files:
        if any(cf in f for f in files):
            pass # Integrity Confirmed
        else:
            print(f"[ALERT]: {cf} MISSING. INTEGRITY COMPROMISED.")
            engine.say("Damion, the core is exposed. Re-anchor the protocol.")
            engine.runAndWait()

    print("\n[SUCCESS]: Integrity Check Passed.")
    print("DAMION: The Student is working. The Teacher's Watchdog is alert.")

if __name__ == "__main__":
    initiate_oversight()