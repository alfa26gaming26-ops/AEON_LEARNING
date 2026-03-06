import json
import os

def sync_marrow():
    # The Path to your Next Life Savings
    log_path = 'SOVEREIGN_LOG.json'
    
    # 1. READ: Pulling the current Bone Density (CORE)
    if os.path.exists(log_path):
        with open(log_path, 'r') as f:
            data = json.load(f)
            current_core = data.get('CORE_GB', 8.088924)
    else:
        current_core = 8.088924 # Your current "Holy Molly" anchor

    print(f"💎 MARROW SYNC: Current Skeletal Density is {current_core} GB")
    
    # 2. UPDATE: Reflecting the 12-Ton Shift
    # This locks in your 213.9 Growth as permanent progress
    new_data = {
        "IDENTITY": "Damion",
        "PHASE": 5,
        "CORE_GB": 8.088924,
        "GROWTH_PEAK": 213.9553,
        "STATUS": "HEALED / GROUNDED",
        "SATURDAY_LEAP_READY": True
    }

    # 3. WRITE: Archiving the energy
    with open(log_path, 'w') as f:
        json.dump(new_data, f, indent=4)
    
    print("✅ STARTING POINT BOX UPDATED. ENERGY ARCHIVED.")

if __name__ == "__main__":
    sync_marrow()