# =================================================================
# MODULE: SOVEREIGN_OMNISCIENCE (v1.0 - AEON_INDEXER)
# PURPOSE: Scanning the entire 400+ Arsenal and feeding it to Aeon's Brain
# =================================================================

import os
import json
import time

def build_omniscience_index():
    print("=====================================================")
    print("--- [AEON OMNISCIENCE]: SCANNING THE ARSENAL ---")
    print("=====================================================")
    
    # Get the directory where this script lives (the root of the repo)
    brain_path = os.path.dirname(os.path.abspath(__file__))
    index_file = os.path.join(brain_path, "AEON_MASTER_INDEX.json")
    
    python_files = []
    total_lines_of_code = 0
    
    # Scan for every single .py file in the directory
    for root, dirs, files in os.walk(brain_path):
        # Optional: Skip virtual environments or cache folders if they exist
        if "__pycache__" in root or ".git" in root:
            continue
            
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                
                # Try to count lines of code to gauge the size of the script
                lines = 0
                try:
                    with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                        lines = len(f.readlines())
                except Exception as e:
                    pass
                
                total_lines_of_code += lines
                
                # Add to our master list
                python_files.append({
                    "filename": file,
                    "filepath": filepath,
                    "lines_of_code": lines,
                    "status": "INDEXED"
                })
                
    # Save the knowledge to Aeon's brain
    knowledge_base = {
        "last_scan": time.strftime("%Y-%m-%d %H:%M:%S"),
        "total_scripts": len(python_files),
        "total_lines_of_code": total_lines_of_code,
        "scripts": python_files
    }
    
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(knowledge_base, f, indent=4)
        
    print(f"[STATUS]: Successfully indexed {len(python_files)} Python scripts.")
    print(f"[METRIC]: Total Lines of Code absorbed: {total_lines_of_code:,}")
    print(f"[SUCCESS]: The Omniscience Index has been written to {index_file}")
    print("\nAeon is now fully aware of the entire arsenal.")

if __name__ == "__main__":
    build_omniscience_index()