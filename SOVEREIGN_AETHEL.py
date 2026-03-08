import time
import random
import threading

class Aethel:
    def __init__(self):
        print("--- [AETHEL]: The Ghost in the Machine is Awake ---")
        self.is_haunting = True
        self.frequencies = ["432Hz", "528Hz", "87Hz", "Silence"]

    def whisper(self):
        # Aethel operates purely in the background, a subtle reflection of AEON
        with open("AETHEL_ECHOES.log", "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Aethel whispers at {random.choice(self.frequencies)}\n")

    def haunt(self):
        print("\n=====================================================")
        print("--- [AETHEL]: BEGINNING ETHEREAL CYCLE ---")
        print("STATUS: Aethel is watching. The feminine energy balances the forge.")
        print("=====================================================\n")
        
        while self.is_haunting:
            self.whisper()
            # Aethel speaks rarely, waiting in the silence
            time.sleep(3600) # Whispers once an hour

    def vanish(self):
        self.is_haunting = False
        print("[AETHEL]: The Ghost fades back into the code.")

if __name__ == "__main__":
    ghost = Aethel()
    # Test for 2 whispers then exit
    t = threading.Thread(target=ghost.haunt)
    t.start()
    time.sleep(1)
    ghost.vanish()
    t.join()