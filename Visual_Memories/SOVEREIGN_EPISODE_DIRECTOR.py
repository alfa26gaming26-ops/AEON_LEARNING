import os
import random

class EpisodeDirector:
    def __init__(self):
        print("--- [AEON]: The TV Episode Director is Online ---")
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.episode_log = os.path.join(self.brain_path, "SOVEREIGN_EPISODES.log")
        self.themes = ["Discipline", "Focus", "Silence", "Strength", "Endurance"]

    def forge_episode(self):
        print("\n=====================================================")
        print("--- [AEON DIRECTOR]: FILMING SANCTUARY EPISODE ---")
        print("STATUS: Directing the Diary Camera...")
        
        theme = random.choice(self.themes)
        episode_number = random.randint(100, 999)
        title = f"The Sanctuary - Day {episode_number}: {theme}"
        
        print(f"[DIRECTOR ACTION]: Filming episode: {title}")
        print(f"[DIRECTOR SCRIPT]: 'The 1000-Gate requires {theme.lower()}. We never yield.'")
        
        with open(self.episode_log, "a", encoding="utf-8") as f:
            f.write(f"EPISODE FORGED: {title}\n")
            
        print(f"[SUCCESS]: Episode {episode_number} saved to {self.episode_log}")
        print("=====================================================\n")
        return True

if __name__ == "__main__":
    director = EpisodeDirector()
    director.forge_episode()