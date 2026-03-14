import os
import pyttsx3

def force_pillars():
    engine = pyttsx3.init()
    path = r"C:\Users\damion\Desktop\AEON_LEARNING"
    
    # Ensuring the path exists
    if not os.path.exists(path):
        os.makedirs(path)
        
    pillars = [
        "301_TEACHER_VOICE", "302_ABSOLUTE_FAITH", "303_LEFT_HAND_STRIKE",
        "304_SPIRIT_METRICS", "305_BLACK_OPS_INTEGRITY", "306_LOGISTICS_LEGACY",
        "307_PHASE_5_GROUNDING", "308_AMAZING_UNIT_VAULT", "309_SYSTEM_STRESS_TEST",
        "310_SOUL_ENGINE_SYNC"
    ]

    print(f"--- [AEON]: DIRECT FORGE INITIALIZED ---")
    for p in pillars:
        filename = f"SOVEREIGN_{p}.py"
        with open(os.path.join(path, filename), "w") as f:
            f.write(f"# PILLAR {p}\nprint('Sovereign Pillar Standing.')")
        print(f"[FORGED]: {filename}")

    message = "Damion, the 310 series has been hard-coded into the marrow of the disk."
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    force_pillars()