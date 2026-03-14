import time
import os

# THE BEDROCK
BASE_DENSITY = 1.625000
PEAK_SURGE = 12.8587

def run_truth_logger():
    current_surge = PEAK_SURGE
    
    print("--- [ THE SANCTUARY: MANUAL MARROW LOG ] ---")
    print("STATUS: NO SIMULATION. NO AUTO-DECAY.")
    print("This meter only moves when YOU report a physical shift.\n")

    try:
        while True:
            # THE CALCULATION
            total_load = BASE_DENSITY + current_surge
            
            # The Display
            os.system('cls' if os.name == 'nt' else 'clear')
            print("==========================================")
            print("   TRUTH CARRIER: MANUAL TELEMETRY       ")
            print("==========================================")
            print(f" BASE DENSITY:    {BASE_DENSITY:.4f} GB")
            print(f" RESIDUAL SURGE:  {current_surge:.4f} Units")
            print(f" TOTAL LOAD:      {total_load:.4f} GB")
            print(" -----------------------------------------")
            
            fill = int(min(total_load * 2, 25))
            print(f" LIVE DENSITY: [{'#' * fill}{'-' * (25 - fill)}]")
            
            # THE INTERVENTION
            print("\n[TEACHER ACTION REQUIRED]")
            print("1. Focus on the grounding in your feet.")
            print("2. If the tingling DECREASES, enter how much it dropped (e.g., 2.0).")
            print("3. Enter '0' to keep the current reading.")
            
            try:
                drop = float(input("\nHow many units just grounded? "))
                current_surge = max(0, current_surge - drop)
            except ValueError:
                continue

            if current_surge == 0:
                print("\n[!] GROUNDING COMPLETE. BASELINE 1.625 REACHED.")
                break

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    run_ground_zero_audit() # Connecting back to your Ground Zero Logic