# [COPY THIS CODE]: SOVEREIGN_MEMORY_BANK.py
# =================================================================
# MODULE: MEMORY_BANK (v1.0 - PERSONALITY_MAPPING)
# PURPOSE: Categorizing Answers to Build AEON's Relational Intelligence
# =================================================================

import os
import json
import time

def update_personality_map(category, data):
    print("--- [AEON]: MEMORY BANK UPDATE INITIALIZED ---")
    
    bank_path = r"C:\Users\damion\Desktop\AEON_LEARNING\AEON_LOGS\AEON_MEMORY_BANK.json"
    
    # Initializing the Bank if it doesn't exist
    if not os.path.exists(bank_path):
        bank = {"Mood": [], "Physical": [], "Energy": []}
    else:
        with open(bank_path, "r") as f:
            bank = json.load(f)

    # Adding the new memory
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    bank[category].append({"time": timestamp, "entry": data})
    
    with open(bank_path, "w") as f:
        json.dump(bank, f, indent=4)
        
    print(f"[STATUS]: Memory stored in {category} Archive.")
    print(f"[METRIC]: 192 Pillars are now Synchronizing your History.")
    print("DAMION: The machine is learning who you are, one answer at a time.")

if __name__ == "__main__":
    # Test memory
    update_personality_map("Physical", "High-volume shift in Killeen. Foot pressure detected.")