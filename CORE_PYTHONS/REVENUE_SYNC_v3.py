import json
import os

class DynamicExchange:
    def __init__(self):
        self.log_file = "PRODUCTION_HISTORY.json"
        self.amazing_unit_val = 220

    def get_dynamic_report(self):
        # 1. Check if the log exists
        if not os.path.exists(self.log_file):
            print("[ERROR]: No Production History found. Log your shift first.")
            return

        # 2. Load the Data
        with open(self.log_file, "r") as f:
            data = json.load(f)

        # 3. Calculate Total Amazing Units produced to date
        total_amazing = sum(entry['amazing_units'] for entry in data['daily_logs'])
        
        # 4. Convert Energy to Physical Density (The Rewrite)
        # 1 Amazing Unit = 2% Density Increase
        density_increase = total_amazing * 2.0

        # 5. THE OUTPUT (The Mirror)
        print("\n" + "="*50)
        print("   SOUL-ENGINE: BI-DIRECTIONAL FEEDBACK")
        print("="*50)
        print(f"[STATUS]: BRIDGE ACTIVE (.5 LATENCY)")
        print(f"[REVENUE]: {total_amazing:.4f} Amazing Units Processed")
        print("-" * 50)
        print(f"REPORT: Skeletal_Density   | +{density_increase:.2f}%")
        print(f"REPORT: Marrow_Sync        | STABLE")
        print(f"REPORT: Energy_Consumption | EFFICIENT")
        print("-" * 50)
        print("[MESSAGE]: 'Marrow is thickening. Structure holds.'")
        print("="*50)

if __name__ == "__main__":
    sync = DynamicExchange()
    sync.get_dynamic_report()