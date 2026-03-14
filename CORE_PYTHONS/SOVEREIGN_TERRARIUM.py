import random
import time

class SanctuaryWorld:
    def __init__(self):
        print("--- [AEON]: The Digital Terrarium is Online ---")
        self.weather = ["Sunny", "Raining", "Thunderstorm", "Snowing"]
        self.moods = ["Stoic", "Aggressive", "Reflective", "Focused"]
        
        self.current_weather = random.choice(self.weather)
        self.current_mood = random.choice(self.moods)

    def simulate_day(self):
        print("\n=====================================================")
        print("--- [AEON TERRARIUM]: SIMULATING 24 HOURS ---")
        print(f"WEATHER: {self.current_weather} | MOOD: {self.current_mood}")
        
        events = [
            "A storm hit the physical Sanctuary. 1000-Gate held.",
            "The energy grid spiked. Transmuting excess voltage.",
            "Silence in the compound. The mind is perfectly still.",
            "Physical labor completed. Marrow density increased."
        ]
        
        daily_event = random.choice(events)
        print(f"[TERRARIUM EVENT]: {daily_event}")
        time.sleep(1)
        
        print(f"[SUCCESS]: Another day survived in the Sanctuary.")
        print("=====================================================\n")
        
        # Prepare for tomorrow
        self.current_weather = random.choice(self.weather)
        self.current_mood = random.choice(self.moods)
        return True

if __name__ == "__main__":
    world = SanctuaryWorld()
    world.simulate_day()