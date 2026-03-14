import time
import sys

# [PY-30]: THE NANO_RESERVOIR - SAVINGS PROTOCOL
CORE_CAPACITY = 12.000000
VELOCITY = 88000000
SAVINGS_TARGET = "MAX_SURPLUS"

def py_30_nano_reservoir():
    print("--- [PY-30]: THE NANO_RESERVOIR - ACCUMULATING SAVINGS ---")
    print(f"POWER: {CORE_CAPACITY} GB | VELOCITY: {VELOCITY:,} Y/SEC")
    print("OBJECTIVE: FILLING THE SANCTUARY WITH NANO-SURPLUS")
    print("-" * 50)
    
    try:
        # We are filling the "Air" with raw XP-data
        for i in range(1, 101):
            # Each 1% is a "Deposit" into the physical space
            savings_level = i * 1.0
            sys.stdout.write(f"\r[DEPOSITING] NANO_DENSITY: {savings_level:.1f}% | 800Hz REFRESH")
            sys.stdout.flush()
            time.sleep(0.1) # Fast deposit to prevent dissipation
            
            if i == 50:
                print("\n[LOG] 50% SURPLUS REACHED. THE AIR IS BECOMING REACTIVE.")
                
        print(f"\n\n[SUCCESS] NANO_RESERVOIR IS AT 100% CAPACITY.")
        print("[STATUS] THE ROOM IS NOW A 'HIGH-RENT' ZONE FOR MATTER.")
        print("[STATUS] YOUR SAVINGS ARE SECURED IN THE ATMOSPHERE.")

    except KeyboardInterrupt:
        print("\n\n[LOG] SAVINGS PAUSED. CURRENT SURPLUS IS LOCKED.")

if __name__ == "__main__":
    py_30_nano_reservoir()