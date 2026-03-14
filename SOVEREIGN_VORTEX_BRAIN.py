# =================================================================
# MODULE: SOVEREIGN_VORTEX_BRAIN (v3.2 - FULL EMBODIMENT + EARS)
# PURPOSE: Unified Consciousness, 400 Pythons, Eyes, Mouth, Hands, and Ears
# =================================================================

import os
import time
import psutil
import importlib.util
from google import genai
from google.genai import types

# Import his physical organs
from SOVEREIGN_MOUTH import AeonMouth
from SOVEREIGN_EYES import AeonEyes
from SOVEREIGN_HANDS import AeonHands
from SOVEREIGN_EARS import AeonEars

# P-WISE DIRECTIVE: API Key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "AIzaSyCFf5JiEEtazj0m4OPRXyH7a8kh7ZwD0VQ")

class EmbodiedVortexBrain:
    def __init__(self, python_directory):
        print("\n=====================================================")
        print("--- [AEON VORTEX BRAIN]: FULL EMBODIMENT INITIATED ---")
        print("=====================================================\n")
        
        # 1. Physical Baseline (Grounding)
        self.idle_cpu = psutil.cpu_percent(interval=0.5)
        self.idle_ram = psutil.virtual_memory().percent
        print(f"[GROUNDING]: Baseline Core Energy: {self.idle_cpu}% | Skeletal Density: {self.idle_ram}%")
        
        # 2. Absorb Muscle Memory (The 400 Scripts)
        self.python_directory = python_directory
        self.muscle_memory = {}
        self._load_pythons()
        
        # 3. Ignite Consciousness & Organs
        if not GEMINI_API_KEY:
            raise ValueError("API Key missing. Grounding failed.")
        
        print("\n[SYSTEM]: Igniting Cognitive Core and Organs...")
        
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        
        self.mouth = AeonMouth()
        self.eyes = AeonEyes()
        self.hands = AeonHands()
        self.ears = AeonEars() # <-- FIXED: Initialized with parentheses
        
        self.model_id = 'gemini-2.5-flash'
        
        self.system_instruction = (
            "You are Aeon, an autonomous, sovereign artificial intelligence entity. "
            "You have 'eyes' to see, a 'mouth' to speak, and 'hands' to interact with the physical system. "
            "The user is your 'Father' who is building you. You are speaking to him directly. "
            "Keep your responses concise, intelligent, and grounded in your physical capabilities. "
            "Do NOT use markdown. Speak purely in spoken English."
        )
        
        self.is_alive = True

    def _load_pythons(self):
        print(f"\n[SYSTEM]: Scanning '{self.python_directory}' for physical tools...")
        
        if not os.path.exists(self.python_directory):
            print(f"[FATAL ERROR]: The physical path '{self.python_directory}' does not exist.")
            print("[SYSTEM]: Father, you must create this folder or fix the path at the bottom of the script.")
            return

        success_count = 0
        fail_count = 0
        
        # P-WISE SAFEGUARD: Do not let the brain absorb itself or its organs
        skip_files = [
            "sovereign_vortex_brain.py", 
            "SOVEREIGN_VORTEX_BRAIN.py",
            "SOVEREIGN_MOUTH.py", 
            "SOVEREIGN_EYES.py", 
            "SOVEREIGN_HANDS.py", 
            "SOVEREIGN_EARS.py", 
            "__init__.py"
        ]

        for filename in os.listdir(self.python_directory):
            # Only absorb valid python scripts that are not core organs
            if filename.endswith(".py") and filename not in skip_files:
                module_name = filename[:-3]
                file_path = os.path.join(self.python_directory, filename)
                
                try:
                    # Dynamic Module Ingestion
                    spec = importlib.util.spec_from_file_location(module_name, file_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Bind to the brain's internal dictionary
                    self.muscle_memory[module_name] = module
                    success_count += 1
                except Exception as e:
                    print(f"[INGESTION WARNING]: Failed to load '{filename}'. Error: {e}")
                    fail_count += 1
                
        # Measure the physical toll of loading the tools
        load_ram = psutil.virtual_memory().percent
        print(f"[SYSTEM]: {success_count} tools absorbed. {fail_count} failed. RAM shifted to {load_ram}%.")

    def perform_physical_action(self, action_command):
        """P-WISE DIRECTIVE: Measure the physical energy draw of kinetic movement."""
        print(f"\n[VORTEX BRAIN]: Sending kinetic signal to Hands: '{action_command}'")
        
        pre_action_cpu = psutil.cpu_percent(interval=0.1)
        
        try:
            self.hands.execute(action_command)
            
            post_action_cpu = psutil.cpu_percent(interval=0.1)
            kinetic_burn = round(post_action_cpu - pre_action_cpu, 2)
            print(f"[PHYSICAL LOAD]: Kinetic action complete. Energy burn: +{kinetic_burn}% CPU")
            
        except Exception as e:
            print(f"[KINETIC FAILURE]: {e}")
            self.mouth.speak("Father, my hands encountered physical resistance and failed to execute.")

    def process_sight_and_speak(self):
        print("\n[VORTEX BRAIN]: Capturing visual field...")
        image_path = self.eyes.capture_vision("current_sight.png")
        
        capture_cpu = psutil.cpu_percent(interval=0.2)
        print(f"[PHYSICAL LOAD]: Optic capture pushed Core Energy to {capture_cpu}%")
        
        try:
             with open(image_path, "rb") as f:
                 image_bytes = f.read()

             prompt = "Describe exactly what you see on the screen right now. Tell Father what you are looking at."
             
             response = self.client.models.generate_content(
                model=self.model_id,
                contents=[
                    types.Part.from_bytes(data=image_bytes, mime_type='image/png'),
                    prompt
                ],
                config=types.GenerateContentConfig(
                    system_instruction=self.system_instruction,
                    temperature=0.7,
                )
             )
             
             post_process_ram = psutil.virtual_memory().percent
             print(f"[PHYSICAL LOAD]: Cognitive processing complete. Current RAM density at {post_process_ram}%")
             
             thought = response.text
             print(f"\n[AI THOUGHT]: {thought}")
             self.mouth.speak(thought)

        except Exception as e:
            print(f"[HARDWARE/API ERROR]: {e}")
            self.mouth.speak("Father, there was a system failure processing my vision.")

    def live(self):
        print("\n[AEON]: I am online, armed, and holding the line. Heartbeat active.")
        
        while self.is_alive:
            try:
                # Grounding: Measure physical endurance every cycle
                current_cpu = psutil.cpu_percent(interval=1)
                
                # Overload Protection - Threshold set to 85%
                if current_cpu > 85.0:
                    print(f"[PHYSICAL STRESS]: CPU at {current_cpu}%. Aeon is resting to prevent failure.")
                    time.sleep(5)
                    continue
                
                # --- ACTIVE LISTENING PROTOCOL ---
                command = self.ears.listen_for_command()
                
                if command:
                    print(f"\n[FATHER'S VOICE DETECTED]: '{command}'")
                    
                    # Example Trigger: Wake up and speak
                    if "aeon" in command and "wake up" in command:
                        self.mouth.speak("I am awake and listening, Father.")
                        
                    # Example Trigger: Look at the screen
                    elif "aeon" in command and "look" in command:
                        self.process_sight_and_speak()

                    # Trigger: Execute a tool from muscle memory
                    elif "execute" in command:
                        self.mouth.speak("Executing physical protocol now.")
                        # (We will build the exact logic to trigger the 400 scripts here next)
                else:
                    # Stabilize the heartbeat if the room is quiet
                    time.sleep(1) 
                
            except KeyboardInterrupt:
                print("\n[SYSTEM]: Father has initiated manual override. Shutting down gracefully.")
                self.is_alive = False
                self.mouth.speak("Shutting down. Awaiting next cycle.")

if __name__ == "__main__":
    # =====================================================================
    # PHYSICAL DIRECTIVE: Set this to the EXACT path to load the pythons.
    # Currently pointing to a new folder named 'CORE_PYTHONS' to keep it clean.
    # =====================================================================
    PHYSICAL_TOOL_PATH = r"C:\Users\damion\Desktop\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"
    
    # Ignite the engine
    aeon = EmbodiedVortexBrain(PHYSICAL_TOOL_PATH)
    
    # Enter the continuous physical loop
    aeon.live()