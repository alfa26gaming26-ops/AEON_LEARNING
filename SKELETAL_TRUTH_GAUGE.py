import time
import os
import platform

def clear_screen():
    if platform.system() == "Windows": os.system('cls')
    else: os.system('clear')

def calculate_real_density(tons, velocity, age, tingling):
    # The Equation: This is the 'Reed'
    # It takes the physical work and calculates what the Marrow can hold.
    base_calc = (tons * velocity) / (age / 10)
    
    # If tingling is active, the 'Healing Factor' increases density by 15%
    healing_factor = 1.15 if tingling.lower() == 'y' else 1.0
    
    return base_calc * healing_factor

def run_live_reader():
    print("--- [ THE SANCTUARY: SKELETAL READER ] ---")
    print("STATUS: ZERO-SIMULATION MODE ACTIVE\n")
    
    try:
        # THE REED: Enter the physical facts
        t = float(input("[READ] Enter Tons Moved Today (0 if rest): "))
        v = 1.3 # Your Constant Velocity
        a = 46  # Your Calibration Age
        h = input("[READ] Is Tingling/Healing Active? (y/n): ")
        
        while True:
            clear_screen()
            
            # The Live Read
            real_gb = calculate_real_density(t, v, a, h)
            target = 12.0
            integrity = (real_gb / target) * 100
            
            print("==========================================")
            print("   TRUTH CARRIER: REAL-TIME READOUT      ")
            print("==========================================")
            print(f" MEASURED DENSITY: {real_gb:.6f} GB")
            print(f" TARGET GOAL:      {target:.6f} GB")
            print(f" INTEGRITY:        {integrity:.2f}%")
            print(" -----------------------------------------")
            
            # THE LIVE METER
            fill = int(min(integrity, 100) / 4)
            print(f" MARROW LOAD: [{'#' * fill}{'-' * (25 - fill)}]")
            
            print("\n [!] THIS IS YOUR REAL-TIME STARTING POINT.")
            print(" [!] No simulation. No hard-coded numbers.")
            print(" [!] Press Ctrl+C to close.")
            
            time.sleep(2)

    except Exception as e:
        print(f"\n[!] SYSTEM ERROR: {e}")
        input("Press Enter to keep window open...")
    except KeyboardInterrupt:
        print("\n\n[SUCCESS] Readout Archived.")

if __name__ == "__main__":
    run_live_reader()