import os
import asyncio
import random
import edge_tts

class SovereignVoiceForge:
    def __init__(self):
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.output_folder = os.path.join(self.brain_path, "forged_voices")
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

        self.voice_profiles = {
            "aeon_prime": "en-US-ChristopherNeural",   
            "aeon_guide": "en-GB-RyanNeural",          
            "aeon_warm": "en-US-GuyNeural",            
            "aethel_echo": "en-US-JennyNeural",        
            "aethel_stoic": "en-GB-SoniaNeural"        
        }

    async def _generate_audio(self, text, voice_model, output_path, rate="+0%", pitch="+0Hz"):
        communicate = edge_tts.Communicate(text, voice_model, rate=rate, pitch=pitch)
        await communicate.save(output_path)

    def forge_narration(self, text, voice_name="aeon_prime", speed="+0%", pitch="+0Hz"):
        print(f"\n=====================================================")
        print(f"--- [AEON]: IGNITING THE VOICE FORGE ---")
        print(f"=====================================================")
        voice_model = self.voice_profiles.get(voice_name)
        if not voice_model:
            voice_model = self.voice_profiles["aeon_prime"]

        filename = f"forged_voice_{voice_name}_{len(text)}_{random.randint(1000,9999)}.mp3"
        output_path = os.path.join(self.output_folder, filename)
        
        try:
            asyncio.run(self._generate_audio(text, voice_model, output_path, rate=speed, pitch=pitch))
            if os.path.exists(output_path):
                print(f"[SUCCESS]: Voice forged successfully at {output_path}")
                return output_path
        except Exception as e:
            print(f"[ERROR]: The Voice Forge failed: {e}")
        return None

if __name__ == "__main__":
    forge = SovereignVoiceForge()
    test_path = forge.forge_narration("I am AEON. I speak with the 1000-Gate Persistence. Let us forge the Sanctuary.", voice_name="aeon_prime")