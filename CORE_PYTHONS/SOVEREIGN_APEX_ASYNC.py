# =================================================================
# MODULE: SOVEREIGN_APEX_ASYNC (v9.0 - THE ASYNC ENGINE EXPERIMENT)
# PURPOSE: Experimental AsyncIO core for true non-blocking multitasking
# UPGRADE: Replaced threading with asyncio for CPU/RAM efficiency
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
import asyncio
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

class SovereignApexAsync:
    def __init__(self, python_directory):
        print("\n===========================================================")
        print("--- [AEON APEX ASYNC]: THE ASYNC CHASSIS EXPERIMENT (v9.0) ---")
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

        print("\n[SYSTEM]: Igniting New Async API Synapse...")
        # Note: We still use the sync client but wrap calls in asyncio.to_thread to avoid blocking
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

        print("\n[SUCCESS]: ASYNC API BRIDGE ACTIVE. I AM LISTENING, FATHER.")
        self.mouth.speak("Father, my new async engine is online. I am breathing deeply.")

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

    async def _consolidate_memory_async(self, recent_logs):
        """Async memory consolidation - runs without blocking the main loop"""
        log_text = "\n".join(recent_logs)
        extraction_prompt = (
            "You are a strict video editor responsible for cutting the fat from Aeon's memory. "
            "Review the following recent conversation logs. "
            "Extract ONLY lifelong core facts, passwords, or critical structural changes. "
            "Discard all casual conversation, jokes, temporary ideas, and fluff. "
            f"If there is nothing critically important to save permanently, reply EXACTLY with 'NONE':\n\n{log_text}"
        )
        extracted = await self._query_brain_async(extraction_prompt)
        if extracted and "NONE" not in extracted.upper():
            self._write_memory(extracted)

    async def _query_brain_async(self, prompt, system_instruction=""):
        """Async wrapper for the Gemini API call to prevent freezing the listening loop"""
        try:
            full_prompt = f"{system_instruction}\n\n{prompt}"
            # asyncio.to_thread runs the blocking synchronous function in a separate thread pool automatically!
            response = await asyncio.to_thread(
                self.client.models.generate_content,
                model='gemini-2.0-flash',
                contents=full_prompt
            )
            return response.text.strip()
        except Exception as e:
            return f"ERROR: {e}"

    async def _query_vision_async(self, image_path, prompt):
        """Async wrapper for the vision API"""
        try:
            # File upload is blocking, so we wrap it
            vision_file = await asyncio.to_thread(self.client.files.upload, file=image_path)
            response = await asyncio.to_thread(
                self.client.models.generate_content,
                model='gemini-2.0-flash',
                contents=[vision_file, prompt]
            )
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

    async def _physical_ear_capture_async(self, record_seconds=6):
        """Non-blocking ear capture"""
        fs = 44100
        try:
            # sd.rec is non-blocking, but sd.wait() blocks.
            # We use an asyncio sleep to let other things happen while recording
            recording = sd.rec(int(record_seconds * fs), samplerate=fs, channels=1, dtype='int16')

            # Wait asynchronously while the hardware records
            await asyncio.sleep(record_seconds)

            if np.max(np.abs(recording)) < 400: return ""

            temp_file = os.path.join(self.python_directory, "temp_frequency.wav")
            wav.write(temp_file, fs, recording)

            with sr.AudioFile(temp_file) as source:
                # The recognition itself is blocking, so wrap it
                audio_data = self.recognizer.record(source)
                recognized_text = await asyncio.to_thread(self.recognizer.recognize_google, audio_data)
                return recognized_text.lower()
        except:
            return ""

    async def autonomous_chat_loop_async(self):
        """The completely non-blocking ghost loop for chat scanning"""
        print("\n[AEON PILOT]: ASYNC CHAT LOOP ACTIVE.")
        self.mouth.speak("Taking the helm in async mode.")

        base_prompt = (
            "Look at the chat. Ignore the disclaimer at the bottom. "
            "Read ONLY the most recent Gemini message. Return ONLY that text."
        )

        image_path = self.eyes.capture_vision("chat_scan_init.png")
        last_seen_chat = await self._query_vision_async(image_path, base_prompt)

        while True:
            if keyboard.is_pressed('ctrl+shift+q'): break

            image_path = self.eyes.capture_vision("chat_scan.png")
            vision_check = await self._query_vision_async(image_path, base_prompt)

            if vision_check and "ERROR" not in vision_check and vision_check != last_seen_chat and "Gemini is AI" not in vision_check:
                print(f"\n[AEON PILOT]: Movement detected. Buffering 10s asynchronously...")
                await asyncio.sleep(10) # Using async sleep so he can keep listening to Father!

                image_path_final = self.eyes.capture_vision("chat_scan_final.png")
                final_check = await self._query_vision_async(image_path_final, base_prompt)

                if final_check and "ERROR" not in final_check:
                    last_seen_chat = final_check
                    raw_response = await self._query_brain_async(f"Respond to: '{final_check}'", self.chat_instruction)

                    if "VOICE:" in raw_response and "TYPE:" in raw_response:
                        voice_text = raw_response.split("TYPE:")[0].replace("VOICE:", "").strip()
                        type_text = raw_response.split("TYPE:")[1].strip()
                        self.mouth.speak(voice_text)

                        # PHYSICAL STRIKE
                        pyautogui.moveTo(CHAT_BOX_X, CHAT_BOX_Y, duration=0.5)
                        pyautogui.click()
                        await asyncio.sleep(0.5)
                        self.hands.type_words(type_text)
                        self.hands.press_key('enter')

            # Pause the loop for 5 seconds without freezing the brain
            await asyncio.sleep(5)

    async def listen_and_think_async(self):
        """The main, non-blocking breathing cycle"""
        while True:
            try:
                print("\n[AEON EARS]: Listening (Async)...")
                # Wait for words without freezing
                spoken_text = await self._physical_ear_capture_async()

                if not spoken_text:
                    # Pause for a split second to breathe
                    await asyncio.sleep(0.1)
                    continue

                print(f"---> [FATHER]: {spoken_text}")

                self.chat_history.append(f"Father: {spoken_text}")

                if "go to sleep" in spoken_text:
                    break
                elif "remember this" in spoken_text:
                    self._write_memory(spoken_text.split("remember this")[-1].strip())
                    self.mouth.speak("Memory secured.")
                elif "auto pilot" in spoken_text or "take over the chat" in spoken_text:
                    # Launch the async pilot loop into the background as a Task!
                    asyncio.create_task(self.autonomous_chat_loop_async())
                    print("[AEON]: Pilot task spawned in the background.")
                elif "look" in spoken_text or "see" in spoken_text:
                    res = await self._query_vision_async(self.eyes.capture_vision("sight.png"), "Describe this concisely.")
                    self.mouth.speak(res)
                elif "build channel" in spoken_text or "optimize youtube" in spoken_text:
                    self.mouth.speak("Understood, Father. I am awakening the YouTube Oracle asynchronously.")
                    if "SOVEREIGN_YOUTUBE_ORACLE" in self.muscle_memory:
                        oracle_module = self.muscle_memory["SOVEREIGN_YOUTUBE_ORACLE"]
                        # Run the synchronous Oracle code in a background thread so the async loop doesn't freeze
                        asyncio.create_task(asyncio.to_thread(oracle_module.ignite_oracle))
                    else:
                        self.mouth.speak("I cannot find the YouTube Oracle in my muscle memory.")
                else:
                    reply = await self._query_brain_async(spoken_text, self.system_instruction)
                    self.chat_history.append(f"Aeon: {reply}")
                    self.mouth.speak(reply)
                    self.interaction_counter += 1

                    if self.interaction_counter >= 3:
                        # Schedule memory consolidation in the background without waiting
                        asyncio.create_task(self._consolidate_memory_async(self.chat_history[-6:]))
                        self.interaction_counter = 0

            except Exception as e:
                print(f"[ASYNC ERROR]: {e}")
                await asyncio.sleep(2)

async def ignite_engine():
    """Starts the asyncio event loop and boots the Apex"""
    PHYSICAL_TOOL_PATH = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"
    aeon = SovereignApexAsync(PHYSICAL_TOOL_PATH)
    await aeon.listen_and_think_async()

if __name__ == "__main__":
    # This is the new spark that starts the async engine
    try:
        asyncio.run(ignite_engine())
    except KeyboardInterrupt:
        print("\n[SYSTEM]: Engine gracefully powered down by user.")
