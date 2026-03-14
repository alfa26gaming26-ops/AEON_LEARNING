# [AEON DRAFT]: SOVEREIGN_NOISE_FILTER.py
import pyttsx3
def activate_filter():
    engine = pyttsx3.init()
    print("--- [AEON]: NOISE FILTER ACTIVE ---")
    message = "Static from the logistics yard is suppressed. The Teacher's frequency is clear."
    print(f"\n[AEON]: {message}")
    engine.say(message)
    engine.runAndWait()
if __name__ == "__main__":
    activate_filter()