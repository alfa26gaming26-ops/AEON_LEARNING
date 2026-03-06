import os

try:
    print("--- [AEON]: ATTEMPTING MANUAL AUDIT ---")
    files = [f for f in os.listdir() if "SOVEREIGN_" in f]
    print(f"I see {len(files)} Sovereign files.")
    
    with open("TEST_WRITE.txt", "w") as f:
        f.write("The Hand can write to this folder.")
    print("[SUCCESS]: Permission Check Passed.")

except Exception as e:
    print(f"[CRITICAL ERROR]: {e}")

input("\n[STATIONARY]: Press Enter to close this window...")