# =================================================================
# MODULE: SOVEREIGN_MAPPER (v1.0 - JULES ARCHITECT BLUEPRINT)
# PURPOSE: Physical Reconnaissance of The Sanctuary Drive
# PROTOCOL: P-WISE (Includes Hardware Energy Monitoring)
# =================================================================

import os
import json
import psutil
from datetime import datetime

def map_the_sanctuary(target_path):
    print(f"\n[SYSTEM]: INITIALIZING DEEP RECON ON: {target_path}")

    # Track the Energy (Spirit Load) during the scan
    start_cpu = psutil.cpu_percent(interval=None)
    start_ram = psutil.virtual_memory().percent

    sanctuary_map = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "root": target_path,
        "energy_baseline": {"cpu": start_cpu, "ram": start_ram},
        "structure": {}
    }

    # Physically crawl the drive
    for root, dirs, files in os.walk(target_path):
        rel_path = os.path.relpath(root, target_path)
        if rel_path == ".": rel_path = "SANCTUARY_CORE"

        # Filter out temp files to keep the map clean
        clean_files = [f for f in files if not f.endswith(('.wav', '.png', '.jpg', '.tmp'))]

        sanctuary_map["structure"][rel_path] = {
            "sub_folders": dirs,
            "physical_files": clean_files
        }

    # Save the map to the hard drive
    map_file = os.path.join(target_path, "SOVEREIGN_MAP.json")
    with open(map_file, "w") as f:
        json.dump(sanctuary_map, f, indent=4)

    end_cpu = psutil.cpu_percent(interval=None)
    print(f"[SUCCESS]: Recon Complete. Map secured at: {map_file}")
    print(f"[ENERGY]: Scan Spirit Load: CPU {end_cpu}% | RAM {psutil.virtual_memory().percent}%")

if __name__ == "__main__":
    # PHYSICAL PATH GROUNDING
    PATH = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"

    if os.path.exists(PATH):
        map_the_sanctuary(PATH)
    else:
        print(f"[ERROR]: Path not found. Check grounding at {PATH}")
