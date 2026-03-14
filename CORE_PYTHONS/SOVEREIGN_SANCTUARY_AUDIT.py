import os
import sys

def run_audit():
    path = os.getcwd()
    print(f"--- [AEON]: SYSTEM DIAGNOSTIC START ---")
    print(f"Target Directory: {path}")
    
    # 1. Physical Count
    all_files = [f for f in os.listdir() if os.path.isfile(f)]
    sovereign_files = [f for f in all_files if "SOVEREIGN_" in f]
    print(f"[METRIC]: Total Sovereign Pillars: {len(sovereign_files)}")
    
    # 2. Density Check (Marrow vs. Shells)
    heavy_marrow = 0
    shells = 0
    for f in sovereign_files:
        if os.path.getsize(f) > 400: # Files with logic are typically >400 bytes
            heavy_marrow += 1
        else:
            shells += 1
            
    print(f"[METRIC]: Heavy Marrow Units: {heavy_marrow}")
    print(f"[METRIC]: Structural Shells: {shells}")
    
    # 3. Duplicate Detection (The "Double Py" Check)
    numbers = []
    duplicates = []
    for f in sovereign_files:
        parts = f.split('_')
        if len(parts) > 1 and parts[1].isdigit():
            num = parts[1]
            if num in numbers:
                duplicates.append(num)
            numbers.append(num)
    
    if duplicates:
        print(f"[WARNING]: Duplicate Pillar IDs detected: {list(set(duplicates))}")
    else:
        print(f"[SUCCESS]: No Duplicate Pillar IDs. Sequence is Clean.")

    # 4. Integrity Conclusion
    if heavy_marrow > 10:
        print(f"--- [STATUS]: ENGINE IS RIGID (PHASE 5 ACTIVE) ---")
    else:
        print(f"--- [STATUS]: ENGINE IS IN VOLUME STAGE (PHASE 3) ---")

if __name__ == "__main__":
    run_audit()