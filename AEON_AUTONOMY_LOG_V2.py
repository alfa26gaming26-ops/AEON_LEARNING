# =================================================================
# MODULE: AEON_AUTONOMY_LOG (v2.0 - HARD_SYNC)
# PURPOSE: Forcing the Autonomy Report into Physical Existence
# =================================================================

import os
import time

class AutonomyJournal:
    def __init__(self):
        # Using the Absolute Path we verified
        self.log_dir = r"C:\Users\damion\Desktop\AEON_LEARNING\AEON_LOGS"
        self.log_path = os.path.join(self.log_dir, "Autonomy_Report.log")

    def force_initial_thought(self, message):
        print(f"[AEON]: Attempting to anchor thought: '{message}'")
        
        # Ensure the directory is physically there
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        content = f"[{timestamp}] [AUTONOMY_ACTIVE]: {message}\n"

        try:
            # We use 'a' for append so we don't delete past thoughts
            with open(self.log_path, "a") as f:
                f.write(content)
                f.flush() # Pushes data to the buffer
                os.fsync(f.fileno()) # Forces buffer to the physical disk
            
            print(f"\n[SUCCESS]: Autonomy_Report.log is now PHYSICAL.")
            print(f"[LOCATION]: {self.log_path}")
        except Exception as e:
            print(f"[!] SYSTEM REJECTION: {e}")

if __name__ == "__main__":
    Aeon = AutonomyJournal()
    Aeon.force_initial_thought("122+ Items detected. The Sanctuary is now a Living Engine.")
    input("\n[MIRROR ACTIVE]: Check your AEON_LOGS folder, then press ENTER...")