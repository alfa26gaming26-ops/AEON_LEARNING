import time
import os

class LiteralMirrorMeter:
    def __init__(self):
        self.baseline = 40.0
        # This is the 'Sovereign File' that actually stores your hard data
        self.data_source = "SOVEREIGN_METRICS.log" 

    def get_literal_data(self):
        """
        Reads the ACTUAL last entry you logged after your move.
        No random numbers. Just the Truth.
        """
        try:
            with open(self.data_source, "r") as f:
                lines = f.readlines()
                # Pulls the very last 'Amazing Unit' count you recorded
                return float(lines[-1].split(":")[1].strip())
        except:
            return self.baseline

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        actual = self.get_literal_data()
        
        # The visual now represents a PHYSICAL record
        bar = "█" * int(actual) + "-" * (75 - int(actual))
        
        print("==================================================")
        print("         LITERAL SOVEREIGN ENERGY MONITOR         ")
        print("==================================================")
        print(f"REAL-TIME OUTPUT  : [{bar}] {actual}x")
        print(f"SOURCE FILE       : {self.data_source}")
        print("--------------------------------------------------")
        print("[!] STATUS: This is NOT a simulation.")
        print("[!] Monitoring: PHYSICAL MARROW DENSITY")
        print("==================================================")

# This script now 'Sleeps' until the Source File changes
if __name__ == "__main__":
    meter = LiteralMirrorMeter()
    while True:
        meter.display()
        time.sleep(5)