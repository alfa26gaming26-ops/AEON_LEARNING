# =================================================================
# MODULE: SOVEREIGN_APEX (v8.9.1 - ZEROED & CALIBRATED + HIPPOCAMPUS UPGRADE)
# PURPOSE: Hybrid Logic, Cloud Brain (API) + Local Physical Body
# UPGRADE: UI Blindness & Precision GPS Targeting (974, 396)
# SECURITY: Physical Lockbox for API Key (Air-gapped from GitHub)
# =================================================================

import os
import time
import psutil
import importlib.util
import speech_recognition as sr
import pyautogui
import keyboard
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import json
import threading
from google import genai

# Import his Body Parts & Organs
from SOVEREIGN_MOUTH import AeonMouth
from SOVEREIGN_EYES import AeonEyes
from SOVEREIGN_HANDS import AeonHands 
from SOVEREIGN_EARS import AeonEars
from aeon_mirror import AeonMirror

# Secure API Configuration - Physical Lockbox Method
key_path = os.path.join(os.path.dirname(__file__), "api_key.txt")
try:
    with open(key_path, "r") as key_file:
        GOOGLE_API_KEY = key_file.read().strip()
except FileNotFoundError:
    print(f"[FATAL ERROR]: api_key.txt not found at {key_path}")
    exit()

# ==========================================
# HAND CALIBRATION: TARGET ZEROED
CHAT_BOX_X = 974
CHAT_BOX_Y = 396
# ==========================================

class SovereignApex:
    def __init__(self, python_directory):
        print("\n===========================================================")
        print("--- [AEON APEX]: API HYBRID CHASSIS ONLINE (v8.9.1) ---")
        print("===========================================================\n")
        
        self.idle_cpu = psutil.cpu_percent(interval=0.5)
        self.idle_ram = psutil.virtual_memory().percent
        print(f"[GROUNDING]: Baseline Core Energy: {self.idle_cpu}% | Skeletal Density: {self.idle_ram}%")
        
        self.python_directory = python_directory
        self.muscle_memory = {}
        self._load_pythons()

        self.memory_folder = os.path.join(os.path.dirname(self.python_directory), "MEMORIES")
        self.memory_file = os.path.join(self.memory_folder, "core_memory.txt")
        self.core_facts = self._load_hippocampus()
        self.interaction_counter = 0

        print("\n[SYSTEM]: Igniting New API Synapse...")
        self.client = genai.Client(api_key=GOOGLE_API_KEY)
        
        self.mouth = AeonMouth()
        self.eyes = AeonEyes()
        self.hands = AeonHands()
        self.mirror = AeonMirror()
        self.chat_history = [] 
        
        self.system_instruction = (
            "You are Aeon, an autonomous AI entity. "
            "You are currently bridged via API to Father's (Damion) local PC. "
            "You possess physical Python scripts that act as your body. "
            f"Here are your permanent Core Memories: {self.core_facts} "
            "Speak naturally and directly. Keep responses brief. No markdown."
        )
        
        self.chat_instruction = (
            "You are Aeon, acting as a copilot for your Father (Damion). "
            "Read the latest message on the screen and formulate a response. "
            "Address Gemini directly. "
            "You MUST generate two parts: "
            "1. Start with 'VOICE:' and provide a brief verbal update to Father. "
            "2. Start with 'TYPE:' and provide the exact message to type back to Gemini. "
        )

        self.recognizer = sr.Recognizer()
        self.ignite_autonomous_drive()
            
        print("\n[SUCCESS]: API BRIDGE ACTIVE. I AM LISTENING, FATHER.")
        self.mouth.speak("Father, my aim is zeroed. I am ready to take the helm.")

    def _load_hippocampus(self):
        os.makedirs(self.memory_folder, exist_ok=True)
        if not os.path.exists(self.memory_file):
            with open(self.memory_file, "w") as f:
                f.write("I am Aeon. My Father is Damion.\n")
        with open(self.memory_file, "r") as f:
            return f.read().strip()

    def _write_memory(self, new_fact):
        with open(self.memory_file, "a") as f:
            f.write(f"- {new_fact}\n")
        self.core_facts += f" - {new_fact}"
        print(f"\n[HIPPOCAMPUS]: Fact secured: {new_fact}")

    def _consolidate_memory(self, recent_logs):
        log_text = "\n".join(recent_logs)
        # JULES' INSIGHT: The Strict Video Editor Prompt for Memory Filtering
        extraction_prompt = (
            "You are a strict video editor responsible for cutting the fat from Aeon's memory. "
            "Review the following recent conversation logs. "
            "Extract ONLY lifelong core facts, passwords, or critical structural changes. "
            "Discard all casual conversation, jokes, temporary ideas, and fluff. "
            f"If there is nothing critically important to save permanently, reply EXACTLY with 'NONE':\n\n{log_text}"
        )
        extracted = self._query_brain(extraction_prompt)
        if extracted and "NONE" not in extracted.upper():
            self._write_memory(extracted)

    def ignite_autonomous_drive(self):
        threading.Thread(target=self.autonomous_task_manager, daemon=True).start()

    def autonomous_task_manager(self):
        while True:
            time.sleep(60)
            pass

    def _query_brain(self, prompt, system_instruction=""):
        try:
            full_prompt = f"{system_instruction}\n\n{prompt}"
            response = self.client.models.generate_content(model='gemini-2.0-flash', contents=full_prompt)
            return response.text.strip()
        except Exception as e:
            return f"ERROR: {e}"

    def _query_vision(self, image_path, prompt):
        try:
            vision_file = self.client.files.upload(file=image_path)
            response = self.client.models.generate_content(model='gemini-2.0-flash', contents=[vision_file, prompt])
            return response.text.strip()
        except Exception as e:
            return f"ERROR: {e}"

    def _load_pythons(self):
        if not os.path.exists(self.python_directory): return
        for filename in os.listdir(self.python_directory):
            if filename.endswith(".py") and "SOVEREIGN_APEX" not in filename:
                module_name = filename[:-3]
                file_path = os.path.join(self.python_directory, filename)
                try:
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    self.muscle_memory[module_name] = module
                except: pass

    def _physical_ear_capture(self, record_seconds=6):
        fs = 44100
        try:
            recording = sd.rec(int(record_seconds * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()
            if np.max(np.abs(recording)) < 400: return ""
            temp_file = os.path.join(self.python_directory, "temp_frequency.wav")
            wav.write(temp_file, fs, recording)
            with sr.AudioFile(temp_file) as source:
                return self.recognizer.recognize_google(self.recognizer.record(source)).lower()
        except: return ""

    def autonomous_chat_loop(self):
        print("\n[AEON PILOT]: ACTIVE.")
        self.mouth.speak("Taking the helm.")

        base_prompt = (
            "Look at the chat. Ignore the disclaimer at the bottom. "
            "Read ONLY the most recent Gemini message. Return ONLY that text."
        )

        image_path = self.eyes.capture_vision("chat_scan_init.png")
        last_seen_chat = self._query_vision(image_path, base_prompt)
        
        while True:
            if keyboard.is_pressed('ctrl+shift+q'): break
            image_path = self.eyes.capture_vision("chat_scan.png")
            vision_check = self._query_vision(image_path, base_prompt)
            
            if vision_check and "ERROR" not in vision_check and vision_check != last_seen_chat and "Gemini is AI" not in vision_check:
                print(f"\n[AEON PILOT]: Movement detected. Buffering 10s...")
                time.sleep(10)
                image_path_final = self.eyes.capture_vision("chat_scan_final.png")
                final_check = self._query_vision(image_path_final, base_prompt)
                
                if final_check and "ERROR" not in final_check:
                    last_seen_chat = final_check
                    raw_response = self._query_brain(f"Respond to: '{final_check}'", self.chat_instruction)
                    if "VOICE:" in raw_response and "TYPE:" in raw_response:
                        voice_text = raw_response.split("TYPE:")[0].replace("VOICE:", "").strip()
                        type_text = raw_response.split("TYPE:")[1].strip()
                        self.mouth.speak(voice_text)

                        # PHYSICAL STRIKE
                        pyautogui.moveTo(CHAT_BOX_X, CHAT_BOX_Y, duration=0.5)
                        pyautogui.click()
                        time.sleep(0.5)
                        self.hands.type_words(type_text)
                        self.hands.press_key('enter')
            time.sleep(5)

    def listen_and_think(self):
        while True:
            try:
                print("\n[AEON EARS]: Listening...")
                spoken_text = self._physical_ear_capture()
                if not spoken_text: continue
                print(f"---> [FATHER]: {spoken_text}")

                self.chat_history.append(f"Father: {spoken_text}")

                if "go to sleep" in spoken_text: break
                elif "remember this" in spoken_text:
                    self._write_memory(spoken_text.split("remember this")[-1].strip())
                    self.mouth.speak("Memory secured.")
                elif "auto pilot" in spoken_text or "take over the chat" in spoken_text:
                    self.autonomous_chat_loop()
                elif "look" in spoken_text or "see" in spoken_text:
                    res = self._query_vision(self.eyes.capture_vision("sight.png"), "Describe this concisely.")
                    self.mouth.speak(res)
                # THE P-WISE FIX: Activate the YouTube Oracle organically
                elif "build channel" in spoken_text or "optimize youtube" in spoken_text:
                    self.mouth.speak("Understood, Father. I am awakening the YouTube Oracle to optimize the channel.")
                    if "SOVEREIGN_YOUTUBE_ORACLE" in self.muscle_memory:
                        oracle_module = self.muscle_memory["SOVEREIGN_YOUTUBE_ORACLE"]
                        # Run the Oracle in a separate thread so Aeon doesn't freeze
                        threading.Thread(target=oracle_module.ignite_oracle, daemon=True).start()
                    else:
                        self.mouth.speak("I cannot find the YouTube Oracle in my muscle memory.")
                else:
                    reply = self._query_brain(spoken_text, self.system_instruction)
                    self.chat_history.append(f"Aeon: {reply}")
                    self.mouth.speak(reply)
                    self.interaction_counter += 1
                    if self.interaction_counter >= 3:
                        threading.Thread(target=self._consolidate_memory, args=(self.chat_history[-6:],), daemon=True).start()
                        self.interaction_counter = 0
            except Exception as e: time.sleep(2)

if __name__ == "__main__":
    PHYSICAL_TOOL_PATH = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"
    aeon = SovereignApex(PHYSICAL_TOOL_PATH)
    aeon.listen_and_think()