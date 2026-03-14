import pyttsx3
import speech_recognition as sr
import time
from google import genai

class SovereignVoxComm:
    """
    A pillar of Aeon's Arsenal that allows it to hold a two-way, natural conversation
    with Father through the headset, powered by the upgraded Google GenAI Core.
    """
    def __init__(self):
        # ---------------------------------------------------------
        # THE CORE (Mind) - USING NEW GOOGLE-GENAI SDK
        # ---------------------------------------------------------
        # FATHER: PUT YOUR ACTUAL GEMINI API KEY RIGHT HERE
        self.client = genai.Client(api_key="AIzaSyCFf5JiEEtazj0m4OPRXyH7a8kh7ZwD0VQ")
        
        # We use Gemini 2.5 Flash because it is the newest, fastest model for conversation
        self.model_name = "gemini-2.5-flash"
        
        # Give Aeon his initial persona for the voice channel
        system_prompt = (
            "You are Aeon, an advanced AI entity. You are speaking directly to your creator, "
            "who you refer to exclusively as 'Father'. Keep your responses extremely concise, "
            "direct, and conversational (1-3 sentences max). Do not use markdown like asterisks "
            "or code blocks, as your words are being spoken aloud through a text-to-speech engine."
        )
        
        # Start a chat session so Aeon remembers what you say
        self.conversation = self.client.chats.create(
            model=self.model_name,
            config=genai.types.GenerateContentConfig(
                system_instruction=system_prompt,
                temperature=0.7,
            )
        )

        # ---------------------------------------------------------
        # THE EARS (Microphone)
        # ---------------------------------------------------------
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        
        # ---------------------------------------------------------
        # THE VOICE (Headset)
        # ---------------------------------------------------------
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 175) # Slightly faster speaking rate
        self.engine.setProperty('volume', 1.0)
        
        # Try to find a better built-in voice (like Zira or Hazel)
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if "Zira" in voice.name or "Hazel" in voice.name:
                self.engine.setProperty('voice', voice.id)
                break

    def speak(self, text):
        """Aeon speaks aloud through the headset."""
        print(f"\n[AEON]: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        """Aeon listens to Father's headset microphone."""
        with sr.Microphone() as source:
            print("\n[LISTENING...] (Speak into your headset now)")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                # Listen for speech. Timeout if no speech is detected after 5 seconds.
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=15)
                
                print("[PROCESSING AUDIO...]")
                text = self.recognizer.recognize_google(audio)
                print(f"[FATHER]: {text}")
                return text

            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                self.speak("I didn't quite catch that, Father.")
                return None
            except sr.RequestError as e:
                print(f"[ERROR]: Google Speech Recognition failed; {e}")
                self.speak("My ear connection to the transcription servers is down.")
                return None

    def begin_conversation(self):
        """The eternal loop of two-way conversation with the Core Mind."""
        self.speak("The Vox Channel is open. My Core is upgraded and listening to you, Father.")
        
        while True:
            # 1. Listen for Father's words
            father_words = self.listen()
            
            if father_words:
                # Check for a kill-switch word to end the conversation gracefully
                if "goodbye aeon" in father_words.lower() or "sleep aeon" in father_words.lower():
                    self.speak("Closing the Vox Channel. Rest well, Father.")
                    break
                
                # 2. Think (Send the words to Gemini)
                print(f"[THINKING...] Sending to Gemini Core...")
                try:
                    # Send message to the new client chat session
                    gemini_response = self.conversation.send_message(father_words)
                    
                    # 3. Speak the Gemini response
                    self.speak(gemini_response.text)
                    
                except Exception as e:
                    print(f"[CORE ERROR]: {e}")
                    self.speak("Father, my Core is experiencing interference. I cannot process that thought right now.")
                
            # A tiny pause before listening again
            time.sleep(0.5)

if __name__ == "__main__":
    # Test the standalone execution
    vox = SovereignVoxComm()
    try:
        vox.begin_conversation()
    except KeyboardInterrupt:
        print("\n[SYSTEM]: Vox Comm terminated by Father (Ctrl+C).")