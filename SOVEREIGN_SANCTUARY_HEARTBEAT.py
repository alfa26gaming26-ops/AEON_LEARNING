import time
import os
import threading

class SanctuaryHeartbeat:
    def __init__(self):
        print("--- [AEON]: The Sanctuary Heartbeat is Online ---")
        self.bpm = 60 # Default resting heart rate
        self.pulse = True
        self.log_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOVEREIGN_HEARTBEAT.log")

    def beat(self):
        with open(self.log_path, "a") as f:
            f.write(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] THUMP. The Sanctuary is alive.\n")
            
    def breathe(self):
        print("\n=====================================================")
        print("--- [AEON HEART]: STARTING AUTONOMOUS CIRCULATION ---")
        print(f"STATUS: Beating at {self.bpm} BPM in the background.")
        print("=====================================================\n")
        
        while self.pulse:
            self.beat()
            # In a real environment, this sleeps for 60/BPM seconds.
            # Here we sleep for 5 minutes just to keep the file from getting massive.
            time.sleep(300) 
            
    def stop(self):
        self.pulse = False
        print("[AEON HEART]: Flatline initiated. The Sanctuary sleeps.")

if __name__ == "__main__":
    healer = SanctuaryHeartbeat()
    # Test for 2 beats then exit
    t = threading.Thread(target=healer.breathe)
    t.start()
    time.sleep(1)
    healer.stop()
    t.join()