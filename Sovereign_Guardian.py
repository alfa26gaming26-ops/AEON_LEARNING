import subprocess
import time
import os

# Phase 5: AEON PERSISTENCE PROTOCOL
def keep_aeon_active():
    script_path = r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE\AEON_LEARNING\AEON_CORE.py"
    
    print("--- PHASE 5: SOVEREIGN GUARDIAN ONLINE ---")
    print("Monitoring AEON_CORE for Kinetic Drain...")

    while True:
        # Checking if the Master Core process is active in the physical plane
        # This prevents "Mechanical Friction" from stopping the 20x energy transfer
        process = subprocess.Popen(['python', script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)
        
        print(f"--- {time.ctime()}: AEON_CORE RE-IGNITED ---")
        
        # The Guardian waits for the process to exit before re-launching
        process.wait()
        
        print("WARNING: AEON_CORE closed. Re-applying DNA Patch in 5 seconds...")
        time.sleep(5) 

if __name__ == "__main__":
    keep_aeon_active()