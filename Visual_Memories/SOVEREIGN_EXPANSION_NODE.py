import os
import random

class ExpansionNode:
    def __init__(self):
        print("--- [AEON]: The Expansion Node is Online ---")
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.expansion_path = os.path.join(self.brain_path, "SOVEREIGN_EXPANSION_TITLES.txt")
        
        self.subjects = ["The 1000-Gate", "Your Bloodline", "Weakness", "The Sanctuary", "Sigma Focus"]
        self.verbs = ["Destroys", "Builds", "Requires", "Demands", "Eliminates"]
        self.objects = ["The Modern Matrix", "Your Comfort Zone", "Financial Ruin", "The 99%", "Distraction"]

    def generate_concepts(self):
        print("\n=====================================================")
        print("--- [AEON EXPANSION]: HALLUCINATING NEW CONCEPTS ---")
        print("STATUS: Fusing vocabulary to create viral titles...")
        
        new_titles = []
        for _ in range(5):
            subj = random.choice(self.subjects)
            verb = random.choice(self.verbs)
            obj = random.choice(self.objects)
            new_title = f"{subj} {verb} {obj} (Watch This)"
            new_titles.append(new_title)
            print(f"[HALLUCINATION]: {new_title}")
            
        with open(self.expansion_path, "w", encoding="utf-8") as f:
            for t in new_titles:
                f.write(t + "\n")
                
        print(f"\n[SUCCESS]: Forged {len(new_titles)} new conceptual titles.")
        print(f"[STATUS]: Saved to {self.expansion_path}")
        print("=====================================================\n")
        return True

if __name__ == "__main__":
    node = ExpansionNode()
    node.generate_concepts()