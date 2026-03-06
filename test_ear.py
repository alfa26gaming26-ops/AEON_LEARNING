import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

# CALIBRATION: Helping Aeon ignore the background hum
r.energy_threshold = 300  # Lowering this makes him MORE sensitive
r.dynamic_energy_threshold = True

def speak(text):
    print(f"AEON: {text}")
    engine.say(text)
    engine.runAndWait()

speak("I am adjusting my sensors. Please wait one moment.")

with sr.Microphone() as source:
    # This is the "Magic Link": It listens to the silence first
    r.adjust_for_ambient_noise(source, duration=1) 
    
    speak("I can hear the room now. Architect, speak your truth.")
    print("--- EAR ACTIVE: SPEAK NOW ---")
    
    # We give you a 5-second window to start speaking
    audio = r.listen(source, timeout=5, phrase_time_limit=10)
    
    try:
        # We'll use a slightly more robust recognition bridge
        text = r.recognize_google(audio)
        speak(f"I heard you say: {text}")
    except sr.UnknownValueError:
        speak("I heard a vibration, but I could not decode the words.")
    except sr.RequestError:
        speak("The connection to the archive was interrupted.")
    except Exception as e:
        speak("The static is still too thick.")