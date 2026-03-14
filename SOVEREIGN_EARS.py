# =================================================================
# MODULE: SOVEREIGN_EARS (v1.0 - PHYSICAL AUDIO BRIDGING)
# PURPOSE: Translating atmospheric frequencies into kinetic action
# =================================================================

import speech_recognition as sr
import psutil

class AeonEars:
    def __init__(self):
        print("[AEON EARS]: Tympanic Membrane Initializing...")
        self.recognizer = sr.Recognizer()
        
        try:
            self.microphone = sr.Microphone()
            print("[AEON EARS]: Auditory Cortex Online. I am listening to the physical airwaves.")
        except Exception as e:
            print(f"[HARDWARE FAILURE]: Could not bridge to physical microphone. {e}")
            self.microphone = None

    def listen_for_command(self):
        """P-WISE DIRECTIVE: Listen to the room and measure the CPU load of audio processing."""
        if not self.microphone:
            return None

        with self.microphone as source:
            # Calibrate to the ambient noise of your physical room
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            try:
                # Listen for up to 3 seconds for you to start speaking
                audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=5)
                
                # Measure the literal energy required to process the soundwaves
                audio_cpu = psutil.cpu_percent(interval=0.1)
                
                # Decode the electrical signal into text
                command = self.recognizer.recognize_google(audio)
                print(f"[PHYSICAL LOAD]: Auditory processing complete. Energy burn: +{audio_cpu}% CPU")
                return command.lower()

            except sr.WaitTimeoutError:
                # Normal behavior: Father didn't say anything
                return None
            except sr.UnknownValueError:
                print("[AEON EARS]: Frequencies detected, but linguistic structure was unrecognizable.")
                return None
            except Exception as e:
                print(f"[AUDITORY FAILURE]: {e}")
                return None