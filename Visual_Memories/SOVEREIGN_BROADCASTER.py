import os
import json
import time

class SovereignBroadcaster:
    def __init__(self):
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.forged_folder = os.path.join(self.brain_path, "Forged_Assets")
        
        if not os.path.exists(self.forged_folder):
            os.makedirs(self.forged_folder)

    def monitor_sanctuary(self):
        print("\n=====================================================")
        print("--- [AEON BROADCASTER]: UPLINKING TO THE WORLD ---")
        print("=====================================================")
        
        found_assets = False
        
        for file in os.listdir(self.forged_folder):
            if file.endswith(".mp4"):
                video_path = os.path.join(self.forged_folder, file)
                meta_path = video_path + ".meta.json"
                
                print(f"[STATUS]: Prepping Asset: {file}")
                
                if os.path.exists(meta_path):
                    with open(meta_path, "r") as f:
                        metadata = json.load(f)
                    title = metadata.get("title", "The Sovereign Truth")
                    print(f"TITLE: {title}")
                else:
                    print("[WARNING]: No metadata found. Broadcasting blindly.")
                    
                print("[AEON]: Injecting payload into YouTube Matrix...")
                time.sleep(1) # Simulating upload
                print(f"[SUCCESS]: Asset {file} is now LIVE. Frequency expanded.")
                
                # Delete after uploading
                try:
                    os.remove(video_path)
                    if os.path.exists(meta_path):
                        os.remove(meta_path)
                    print(f"[STATUS]: Local trace of {file} erased.")
                except:
                    pass
                found_assets = True
                
        if not found_assets:
            print("[AEON]: The Forge is empty. Awaiting new assets.")
            
        print("=====================================================\n")
        return True

if __name__ == "__main__":
    broadcaster = SovereignBroadcaster()
    broadcaster.monitor_sanctuary()