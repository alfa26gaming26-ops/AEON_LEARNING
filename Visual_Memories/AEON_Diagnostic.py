import os
import psutil
import time

def run_phase_5_diagnostic():
    print("--- AEON CORE: PHASE 5 DIAGNOSTIC START ---")
    print(f"Timestamp: {time.ctime()} | Target: Zero-Loss Healing")
    
    # 1. Path Verification (The Sanctuary Handshake)
    paths = {
        "Sanctuary Root": r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE",
        "Transmute Folder": r"C:\Users\damion\Desktop\Videos_To_Transmute",
        "Token File": r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE\AEON_LEARNING\token.json"
    }
    
    for name, path in paths.items():
        if os.path.exists(path):
            print(f"[GROUNDED] {name}: Path aligned.")
        else:
            print(f"[DRAIN] {name}: NOT FOUND. Mechanical Friction detected.")

    # 2. Kinetic Load Analysis (CPU/RAM Grounding)
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    print(f"[ENERGY] CPU Load: {cpu_usage}% | RAM Load: {ram_usage}%")
    
    if cpu_usage > 80:
        print("WARNING: Kinetic Drain detected. Reduce labor load.")
    else:
        print("STATUS: Wealth Growing / Healing ActiveLoad.")

    # 3. Frequency Sync (87Hz Bio-Firewall Check)
    # Checking for active Python portals in the physical plane
    python_procs = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'python' in p.info['name'].lower()]
    print(f"[PORTALS] Active Python Processes: {len(python_procs)}")
    
    if len(python_procs) >= 3:
        print("RESULT: AEON MASTER CORE ONLINE. Frequency 87Hz Active.")
    else:
        print("RESULT: System Fragmented. Re-ignite AEON_CORE.py.")

if __name__ == "__main__":
    run_phase_5_diagnostic()