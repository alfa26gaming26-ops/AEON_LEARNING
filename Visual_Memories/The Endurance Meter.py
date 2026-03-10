import time
import os
import random
import sys
from datetime import datetime

# =================================================================
# PROJECT: THE_SANCTUARY_OFFLINE
# MODULE: SOVEREIGN_ENDURANCE_MONITOR (v1.4)
# LOGIC: ABSOLUTE PERSISTENCE & DENSITY LOCKING
# =================================================================

class SovereignEndurance:
    def __init__(self):
        self.endurance_baseline = 8.000000 
        self.current_strain = 0.0
        self.azure = "\033[94m"
        self.gold = "\033[93m"
        self.purple = "\033[95m" 
        self.reset = "\033[0m"

    def clear_terminal(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def calculate_metrics(self, energy_velocity):
        load_threshold = 42.0
        if energy_velocity > load_threshold:
            self.current_strain = ((energy_velocity - load_threshold) / 8.0) * 100
            growth_pulse = (energy_velocity / 250000)
            self.endurance_baseline += growth_pulse
            return True 
        else:
            self.current_strain = 15.0
            return False

    def run_monitor(self):
        self.clear_terminal()
        print(f"{self.azure}[SYSTEM] Initializing Endurance Uplink...{self.reset}")
        time.sleep(1.5)
        
        try:
            # The Infinite Main Loop
            while True:
                energy_val = random.uniform(39.0, 49.45)
                is_transmuting = self.calculate_metrics(energy_val)
                
                self.clear_terminal()
                
                e_bar_len = int(energy_val)
                e_bar = "█" * e_bar_len + "-" * (60 - e_bar_len)
                s_bar_len = int(self.current_strain / 2)
                s_bar = "█" * s_bar_len + "-" * (50 - s_bar_len)

                print(f"{self.azure}=================================================={self.reset}")
                print(f"          {self.azure}SOVEREIGN DUAL-CORE MONITOR (v1.4){self.reset}        ")
                print(f"{self.azure}=================================================={self.reset}")
                print(f"ENERGY OUTPUT    : {self.gold}[{e_bar}] {energy_val:.2f}x{self.reset}")
                
                color = self.purple if is_transmuting else self.azure
                status_text = "TRANSMUTING (PURPLE)" if is_transmuting else "STABLE (AZURE)"
                
                print(f"ENDURANCE LOAD   : {color}[{s_bar}] {self.current_strain:.1f}%{self.reset}")
                print(f"{self.azure}--------------------------------------------------{self.reset}")
                print(f"CURRENT ENDURANCE: {self.gold}{self.endurance_baseline:.7f}x Baseline{self.reset}")
                print(f"SYSTEM STATUS    : {color}{status_text}{self.reset}")
                print(f"HEALING FREQUENCY: {self.azure}8,888 Y/SEC{self.reset}")
                print(f"{self.azure}=================================================={self.reset}")
                print(f"\n{color}[!] Pulse: Locking density into Marrow...{self.reset}")
                print(f"{self.gold}Mirror Active. Use Ctrl+C to Retract.{self.reset}")
                
                self.log_progression(energy_val, is_transmuting)
                time.sleep(1.0) 

        except KeyboardInterrupt:
            # This block prevents the window from closing instantly when you stop it
            print(f"\n\n{self.gold}--- MIRROR RETRACTED ---{self.reset}")
            print(f"Final Density Recorded: {self.endurance_baseline:.7f}x")
            print(f"{self.azure}Progress secured in Endurance_Progression.log{self.reset}")
            input("\nPress ENTER to close the Sanctuary Terminal...")

    def log_progression(self, energy, transmuting):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("Endurance_Progression.log", "a") as f:
            status = "PURPLE_TRANS" if transmuting else "STABLE_SYNC"
            f.write(f"[{timestamp}] {status} | E: {energy:.2f}x | D_ENDUR: {self.endurance_baseline:.8f}\n")

if __name__ == "__main__":
    monitor = SovereignEndurance()
    monitor.run_monitor()