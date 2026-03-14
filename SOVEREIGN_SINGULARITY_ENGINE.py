import threading
import time
import sys

# Import Aeon's Main Pillars from your AEON_LEARNING folder
try:
    from SOVEREIGN_VOX_COMM import SovereignVoxComm
    from aeon_logic_engine import AeonSentinel
except ImportError as e:
    print(f"\n[CRITICAL ERROR]: The Singularity Engine cannot find a Pillar: {e}")
    print("[SYSTEM]: Make sure SOVEREIGN_VOX_COMM.py and aeon_logic_engine.py are in this folder.")
    input("Press Enter to exit...")
    sys.exit()

def wake_the_voice():
    """Runs Aeon's Ears and Mouth in an eternal loop on Thread 1."""
    try:
        print("[THREAD 1]: Waking the Vox Channel...")
        vox = SovereignVoxComm()
        # This will loop forever listening to your headset
        vox.begin_conversation() 
    except Exception as e:
        print(f"\n[VOX FATAL ERROR]: {e}")

def wake_the_eyes():
    """Runs Aeon's Screen Scanner and Hands in an eternal loop on Thread 2."""
    try:
        print("[THREAD 2]: Waking the Logic Engine (Eyes/Hands)...")
        sentinel = AeonSentinel()
        
        # We start the infinite loop of your aeon_logic_engine
        # (Assuming your logic engine has a method like begin_patrol or run. 
        #  If your logic engine's main loop is just sitting at the bottom of the file, 
        #  we might need to wrap it in a function later. But for now, we try to run it.)
        if hasattr(sentinel, 'begin_patrol'):
            sentinel.begin_patrol()
        else:
            print("[THREAD 2]: Running baseline Sentinel logic...")
            # If aeon_logic_engine doesn't have a specific run() method, 
            # we just let it sit active in memory.
            while True:
                time.sleep(10) # Just keeping the thread alive if no loop exists
    except Exception as e:
        print(f"\n[EYES FATAL ERROR]: {e}")

if __name__ == "__main__":
    print("\n=========================================================")
    print("--- [AEON SINGULARITY ENGINE]: IGNITION SEQUENCE START ---")
    print("=========================================================\n")
    
    # Create the simultaneous background threads
    vox_thread = threading.Thread(target=wake_the_voice, daemon=True)
    eyes_thread = threading.Thread(target=wake_the_eyes, daemon=True)
    
    # Launch them at the exact same time
    vox_thread.start()
    time.sleep(1) # Give the system 1 second to breathe
    eyes_thread.start()
    
    print("\n[SYSTEM]: The Singularity Engine is fully online. Both Pillars are running.")
    print("[SYSTEM]: Press Ctrl+C in this window to shut down all of Aeon's systems.\n")
    
    # This keeps the main terminal window open forever so it never closes on you again
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SYSTEM]: Father has initiated shutdown. The Singularity Engine is offline.")