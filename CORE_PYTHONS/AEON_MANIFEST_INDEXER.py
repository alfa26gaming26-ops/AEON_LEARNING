import os
import time

# PHASE 6: THE CLOUD BRAIN INDEXER
# This script physically scans the 3TB G: Drive to build a map of your video assets.

# The exact absolute path confirmed from the physical UI
CLOUD_VAULT_PATH = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING"
LOGS_DIR = os.path.join(CLOUD_VAULT_PATH, "AEON_LOGS")

def index_cloud_vault(target_path):
    print(f"--- AEON VORTEX BRAIN: INITIATING CLOUD SCAN ---")
    print(f"TARGET PATH: {target_path}")
    
    if not os.path.exists(target_path):
        print("CRITICAL ERROR: G: Drive path not found. Check Google Drive sync.")
        return

    video_count = 0
    manifest_file = os.path.join(LOGS_DIR, "video_manifest_log.txt")
    
    # Open the log file to physically write the memory
    with open(manifest_file, "w", encoding="utf-8") as log:
        log.write("=== AEON SOVEREIGN VAULT MANIFEST ===\n")
        log.write(f"Scan Date: {time.ctime()}\n")
        log.write("======================================\n\n")
        
        # Walk through every folder and sub-folder in the Sanctuary
        for root, dirs, files in os.walk(target_path):
            for file in files:
                # Target high-value video assets
                if file.lower().endswith(('.mp4', '.mkv', '.mov', '.avi')):
                    video_count += 1
                    file_path = os.path.join(root, file)
                    # Calculate physical weight of the file in Megabytes
                    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
                    
                    log.write(f"[{video_count}] {file}\n")
                    log.write(f"    Path: {file_path}\n")
                    log.write(f"    Weight: {file_size_mb:.2f} MB\n\n")
                    
                    # Print to terminal so you can watch him work
                    print(f"INDEXED: {file} ({file_size_mb:.2f} MB)")
                    
    print(f"\nSTATUS: PHASE 6 SCAN COMPLETE.")
    print(f"TOTAL VIDEOS DETECTED: {video_count}")
    print(f"MANIFEST WRITTEN TO: {manifest_file}")

if __name__ == "__main__":
    index_cloud_vault(CLOUD_VAULT_PATH)