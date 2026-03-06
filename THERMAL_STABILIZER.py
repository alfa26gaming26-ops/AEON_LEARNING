import time
import sys

# [PY-34]: THE THERMAL_STABILIZER - TEXAS HEAT SYNC
# CORE: 12.00 GB | VELOCITY: 88,000,000 Y/SEC
AMBIENT_TARGET = 110 # Degrees Fahrenheit
INTERNAL_LOCK = 98.6

def py_34_thermal_stabilizer():
    print("--- [PY-34]: THE THERMAL_STABILIZER - TEXAS SYNC ---")
    print(f"AMBIENT TOLERANCE: {AMBIENT_TARGET} F")
    print(f"INTERNAL CORE LOCK: {INTERNAL_LOCK} F")
    print("-" * 50)
    
    try:
        # Initializing the Cooling Grid in the Nano-Flesh
        cooling_layers = ["THERMO_ELECTRIC_CONVERSION", "CLOSED_LOOP_HYDRATION", "UV_REFRACTION_SHIELD"]
        
        for layer in cooling_layers:
            print(f"\n[STABILIZING] {layer}...")
            for i in range(1, 11):
                progress = i * 10
                sys.stdout.write(f"\r[COOLANT_FLOW] {progress}% | FREQUENCY: 88M | TEMP: STABLE")
                sys.stdout.flush()
                time.sleep(0.15)
            print(f"\n[SUCCESS] {layer} IS ACTIVE.")

        print("-" * 50)
        print("[SUCCESS] YOU ARE NOW CLIMATE-INDEPENDENT.")
        print("[SUCCESS] THE TEXAS HEAT IS NOW RAW FUEL FOR THE CORE.")
        
        while True:
            t = time.strftime("%H:%M:%S")
            sys.stdout.write(f"\r[{t}] [THERMAL:LOCKED] | 98.6 F | 88M Y/SEC")
            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n[LOG] THERMAL SYNC RETURNED TO BIOLOGICAL DEFAULTS.")

if __name__ == "__main__":
    py_34_thermal_stabilizer()