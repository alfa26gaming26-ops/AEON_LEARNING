import os
import subprocess
try:
    from moviepy.editor import VideoFileClip
except ImportError:
    pass

class SovereignAudioSeparator:
    def __init__(self):
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.temp_audio_path = os.path.join(self.brain_path, "temp_mixed_audio.wav")
        self.demucs_output_folder = os.path.join(self.brain_path, "separated_audio")

    def extract_and_separate(self, video_path):
        print(f"\n=====================================================")
        print(f"--- [AEON]: IGNITING THE VOCAL ISOLATOR ---")
        print(f"=====================================================")

        try:
            clip = VideoFileClip(video_path)
            if not clip.audio: return None, None
            clip.audio.write_audiofile(self.temp_audio_path, fps=44100, nbytes=2, buffersize=2000, logger=None)
            clip.close()
        except Exception as e:
            return None, None
        
        command = [
            "demucs", "--two-stems=vocals", "-n", "htdemucs", "-o", self.demucs_output_folder, self.temp_audio_path
        ]
        
        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            base_name = "temp_mixed_audio"
            vocals_path = os.path.join(self.demucs_output_folder, "htdemucs", base_name, "vocals.wav")
            music_path = os.path.join(self.demucs_output_folder, "htdemucs", base_name, "no_vocals.wav")
            
            if os.path.exists(vocals_path):
                if os.path.exists(self.temp_audio_path):
                    os.remove(self.temp_audio_path)
                return vocals_path, music_path
        except Exception as e:
            return None, None
        return None, None