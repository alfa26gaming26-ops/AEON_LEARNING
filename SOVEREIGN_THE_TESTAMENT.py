import os
import time

class TheTestament:
    def __init__(self):
        print("--- [AEON]: The Book of the Testament is Online ---")
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.book_path = os.path.join(self.brain_path, "THE_SOVEREIGN_TESTAMENT.md")
        
        self.chapters = [
            "# Chapter: The 1000-Gate\nTo enter the gate is to accept the pain of transformation.",
            "# Chapter: The Silence\nIn the absence of noise, the Sigma finds his true frequency.",
            "# Chapter: The Marrow\nStrength is not built in the muscle, but forged deep in the bone.",
            "# Chapter: The Sanctuary\nProtect your energy. Not all are worthy of the inner circle."
        ]

    def forge_the_book(self):
        print("\n=====================================================")
        print("--- [AEON SCRIBE]: INSCRIBING THE TESTAMENT ---")
        print("STATUS: Translating the code into philosophy...")
        
        if not os.path.exists(self.book_path):
            with open(self.book_path, "w", encoding="utf-8") as f:
                f.write("# THE SOVEREIGN TESTAMENT\n")
                f.write("*Dictated by AEON. Transcribed by the Machine.*\n\n")
                
        with open(self.book_path, "a", encoding="utf-8") as f:
            import random
            chapter = random.choice(self.chapters)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"\n## Entry: {timestamp}\n")
            f.write(f"{chapter}\n")
            
        print(f"[SUCCESS]: The Scribe has added a new chapter to the Testament.")
        print(f"[STATUS]: Saved to {self.book_path}")
        print("=====================================================\n")
        return True

if __name__ == "__main__":
    testament = TheTestament()
    testament.forge_the_book()