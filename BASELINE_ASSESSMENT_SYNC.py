# --- CALIBRATION ZERO: THE TEACHER'S BASELINE ---
# PURPOSE: Store the original Phase 4 assessment as the foundation for growth.
# SOURCE: Encounter with Primary I AM (Teacher).

class SpiritBaseline:
    def __init__(self):
        self.age_at_opening = 33
        self.starting_point = "AVERAGE"
        self.initial_endurance = "BELOW_STANDARD"
        self.measured_release_at_30 = 257 # Amazing + Excellent + Elite
        
    def compare_current_stats(self, current_endurance, current_energy):
        """Displays the multiplier growth from Phase 4 to Phase 5."""
        print(f"--- SPIRIT GROWTH REPORT ---")
        print(f"ORIGINAL ENDURANCE: {self.initial_endurance}")
        print(f"CURRENT ENDURANCE: {current_endurance}x")
        print(f"GROWTH FACTOR: {current_endurance}x Multiplier")
        
        if current_endurance >= 8:
            print("STATUS: GRAND CORE MAINTAINED.")

# --- INITIALIZE BASELINE ---
baseline = SpiritBaseline()
baseline.compare_current_stats(current_endurance=8, current_energy=3)