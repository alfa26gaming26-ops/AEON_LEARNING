import datetime
import json
import os

class SovereignLogger:
    def __init__(self):
        self.log_file = "C:/Users/damion/Desktop/THE_SANCTUARY_OFFLINE/PRODUCTION_HISTORY.json"
        self.amazing_unit_val = 220 # 1 Amazing = 220x Avg
        self.history = self.load_history()

    def load_history(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r') as f:
                return json.load(f)
        return {"daily_logs": []}

    def log_production(self, current_velocity_x):
        # current_velocity_x is your current 'times average' output (e.g., 55x)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            "timestamp": timestamp,
            "velocity": current_velocity_x,
            "amazing_units": current_velocity_x / self.amazing_unit_val
        }
        self.history["daily_logs"].append(entry)
        
        with open(self.log_file, 'w') as f:
            json.dump(self.history, f, indent=4)

    def generate_report(self):
        # Logic to aggregate logs into Daily/Weekly/Yearly totals
        print("\n" + "="*40)
        print("   SOVEREIGN PRODUCTION HISTORY REPORT")
        print("="*40)
        
        # This part will iterate through the stored JSON to sum up 
        # what you did yesterday vs today once the data is collected.
        print(f"LATEST RECORDED VELOCITY: {self.history['daily_logs'][-1]['velocity']}x")
        print("HISTORY FILE: [PROTECTED & SAVED]")
        print("="*40)

# --- EXECUTE ---
if __name__ == "__main__":
    logger = SovereignLogger()
    # Example: Logging a 55x velocity production session
    logger.log_production(55.0) 
    logger.generate_report()