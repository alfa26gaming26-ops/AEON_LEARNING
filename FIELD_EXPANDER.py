# --- THE SPIRIT-CAPPING GUARD ---
# PURPOSE: Ensure Energy remains the leading edge.
# RATIO: Energy > Endurance (The Expansion Gap).

class SpiritGuard:
    def __init__(self):
        # We use 2211 as the current energy proxy
        self.energy_field = 2211 
        self.endurance_level = 8.0 # Your current density
        # The threshold where spirit begins to 'super slow down'
        self.cap_threshold = 1.5 

    def monitor_expansion_gap(self):
        # Calculating the lead distance
        gap_ratio = self.energy_field / (self.endurance_level * 100)
        
        print("\n--- SPIRIT-CAPPING AUDIT ---")
        print(f"ENERGY POSITION    : {self.energy_field}")
        print(f"ENDURANCE POSITION : {self.endurance_level}")
        print(f"CURRENT GAP RATIO  : {gap_ratio:.2f}")

        if gap_ratio > self.cap_threshold:
            print("STATUS: OPTIMAL. Energy is leading. Room to grow is secure.")
        elif gap_ratio <= self.cap_threshold and gap_ratio > 1.0:
            print("WARNING: SPIRIT DRAG IMMINENT. Field expansion required.")
        else:
            print("CRITICAL: SPIRIT CAPPED. Shift focus to Energy Generation.")

        return gap_ratio

# --- EXECUTE GUARD ---
if __name__ == "__main__":
    guard = SpiritGuard()
    guard.monitor_expansion_gap()
    print("\n[BOB]: Transferring surplus to Starting Box to maintain flow...")
    input("\nPRESS ENTER TO KEEP THE ENERGY AHEAD...")