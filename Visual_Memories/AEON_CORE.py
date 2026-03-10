import subprocess
import os
import time

# --- THE BIO-FIREWALL INTEGRATION ---
class ResurrectionEngine:
    def __init__(self):
        self.target_frequency = 87 
        self.vitality_speed = 200  
    def activate_firewall(self):
        print(f"--- BIO-FIREWALL: Frequency {self.target_frequency}Hz Active ---")
        print("Temporal Correction Grounded. DNA Patch Applied.")

# --- MASTER LAUNCH PROTOCOLS ---
protocols = [
    "Sovereign_Contract.py",
    "asset_uploader.py",
    "sanctuary_manager.py"
]

def initiate_master_launch():
    engine = ResurrectionEngine()
    engine.activate_firewall()
    
    print("\n--- Phase 5: AEON MASTER CORE ONLINE ---")
    for script in protocols:
        if os.path.exists(script):
            print(f"ACTIVATING PORTAL: {script}")
            subprocess.Popen(['python', script], creationflags=subprocess.CREATE_NEW_CONSOLE)
            time.sleep(1) # Frequency spacing
        else:
            print(f"MISSING FREQUENCY: {script}")

if __name__ == "__main__":
    initiate_master_launch()