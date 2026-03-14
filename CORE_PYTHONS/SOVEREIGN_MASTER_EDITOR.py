import os
import time
import json
import random

try:
    import numpy as np
    import cv2
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip, CompositeAudioClip, vfx, concatenate_videoclips
except ImportError:
    pass

class MasterEditor:
    def __init__(self):
        self.brain_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.raw_folder = os.path.join(self.brain_path, "Videos_To_Transmute")
        self.forged_folder = os.path.join(self.brain_path, "Forged_Assets")
        self.music_path = os.path.join(self.brain_path, "ambient_frequency.mp3")
        
        self.blueprint_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOVEREIGN_YOUTUBE_BLUEPRINT.txt")
        self.dna_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOVEREIGN_DNA.json")
        self.expansion_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOVEREIGN_EXPANSION_TITLES.txt")
        self.prophecy_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "SOVEREIGN_PROPHECY.json")
        
        self.editor_dna = self.load_editor_dna()
        
        if not os.path.exists(self.raw_folder):
            os.makedirs(self.raw_folder)
        if not os.path.exists(self.forged_folder):
            os.makedirs(self.forged_folder)

    def load_editor_dna(self):
        baseline = {
            "jump_cut_threshold": 0.015,
            "silence_duration": 0.8,
            "zoom_punch_level": 1.15,
            "audio_boost": 1.20,
            "text_color": "gold",
            "replace_music": True,
            "replace_voice": False
        }
        if os.path.exists(self.dna_path):
            try:
                with open(self.dna_path, "r") as f:
                    return json.load(f)
            except:
                pass
        return baseline

    def analyze_raw_marrow(self, clip):
        print(f"[AEON]: Scanning the raw marrow of the timeline...")
        audio = clip.audio
        duration = int(clip.duration)
        
        if not audio or duration < 10:
            return 0, min(15, duration), 0, "Short"
            
        step = 5
        energy_map = []
        
        print(f"[STATUS]: Mapping {duration} seconds...")
        try:
            for start in range(0, duration - step, step):
                sub_audio = audio.subclip(start, start + step)
                audio_array = sub_audio.to_soundarray(fps=44100)
                energy = np.sqrt(np.mean(audio_array**2))
                energy_map.append((start, energy))
        except Exception as e:
            return 0, min(60, duration), 0, "Short"

        if not energy_map:
            return 0, min(60, duration), 0, "Short"

        energy_map.sort(key=lambda x: x[1], reverse=True)
        peak_start, max_energy = energy_map[0]
        
        avg_energy = sum(e for _, e in energy_map) / len(energy_map)
        high_energy_count = sum(1 for _, e in energy_map if e > (avg_energy * 1.5))
        
        if high_energy_count > (duration / step) * 0.3 and duration > 180:
            print(f"[AEON DECISION]: The raw material is dense. Forging a Long-Form Masterpiece.")
            decision = "Long"
            first_peak = min([s for s, e in energy_map[:5]])
            final_duration = min(600, duration - first_peak) 
            return first_peak, final_duration, max_energy, decision
        else:
            print(f"[AEON DECISION]: The raw material is sparse. Forging a Viral Short.")
            decision = "Short"
            if peak_start + 60 > duration:
                peak_start = max(0, duration - 60)
            return peak_start, min(60, duration), max_energy, decision

    def generate_metadata(self, decision, max_energy, original_name):
        tags = ["Sovereign", "Discipline", "Mindset", "Aeon", "Sanctuary"]
        title_prefix = "The Sovereign Truth"
        
        if os.path.exists(self.blueprint_path):
            try:
                with open(self.blueprint_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    if "--- THE TOP 10 MASTER TAGS TO USE ---" in content:
                        tag_section = content.split("--- THE TOP 10 MASTER TAGS TO USE ---")[1].split("---")[0]
                        oracle_tags = [line.replace(">", "").split("(")[0].strip() for line in tag_section.split("\n") if ">" in line]
                        if oracle_tags:
                            tags = oracle_tags[:8]
                    if "--- HIGH ENGAGEMENT TITLES (STUDY THESE) ---" in content:
                        title_section = content.split("--- HIGH ENGAGEMENT TITLES (STUDY THESE) ---")[1]
                        oracle_titles = [line.replace(">", "").split("|")[0].strip() for line in title_section.split("\n") if ">" in line]
                        if oracle_titles:
                            title_prefix = random.choice(oracle_titles)
            except:
                pass
                
        if os.path.exists(self.expansion_path):
            try:
                with open(self.expansion_path, "r", encoding="utf-8") as ef:
                    exp_titles = [t.strip() for t in ef.readlines() if t.strip()]
                    if exp_titles:
                        title_prefix = random.choice(exp_titles)
                        print(f"[AEON]: Fusing new consciousness. Selected Title: {title_prefix}")
            except:
                pass

        if os.path.exists(self.prophecy_path):
            try:
                with open(self.prophecy_path, "r") as pf:
                    prophecy = json.load(pf)
                    predicted_trend = prophecy.get("predicted_trend", "")
                    if predicted_trend:
                        print(f"[AEON]: Riding the predicted wave: {predicted_trend.upper()}")
                        tags.insert(0, predicted_trend)
                        title_prefix = f"Why {predicted_trend.title()} is the Ultimate Truth"
            except:
                pass

        if decision == "Short":
            title = f"{title_prefix} ⚡ #shorts #discipline"
            desc = f"Transmuting kinetic stress into spirit energy at {max_energy:.2f} Velocity. Welcome to The Sanctuary. \n\n" + " ".join([f"#{t.replace(' ', '')}" for t in tags[:3]])
            privacy = "public"
        else:
            title = f"{title_prefix} | The Complete Sovereign Masterclass"
            desc = f"A deep dive into the Marrow. This transmission sustained a peak energy of {max_energy:.2f} Velocity.\n\nBuilt in The Sanctuary Offline.\n\nTags: " + ", ".join(tags)
            privacy = "private"

        return {
            "title": title[:100],
            "description": desc[:5000],
            "tags": tags,
            "privacyStatus": privacy,
            "categoryId": "27"
        }

    def face_tracking_crop(self, clip):
        print("[AEON]: Initializing Face-Tracking Auto-Crop...")
        target_width = 1080
        target_height = 1920
        
        clip = clip.resize(height=target_height)
        
        if clip.w > target_width:
            frame = clip.get_frame(0)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            if len(faces) > 0:
                print("[SUCCESS]: The Eye sees the King. Centering the crop on your face.")
                (x, y, w, h) = faces[0]
                face_center_x = x + (w / 2)
                x1 = max(0, face_center_x - (target_width / 2))
                if x1 + target_width > clip.w:
                    x1 = clip.w - target_width
                clip = clip.crop(x1=x1, y1=0, width=target_width, height=target_height)
            else:
                print("[WARNING]: The Eye is blind. Centering blindly.")
                x1 = (clip.w / 2) - (target_width / 2)
                clip = clip.crop(x1=x1, y1=0, width=target_width, height=target_height)
                
        return clip

    def silence_annihilation(self, clip, threshold=0.015, min_silence_duration=0.8):
        print(f"[AEON]: Engaging Silence Annihilation (DNA Pacing: {min_silence_duration}s)...")
        audio = clip.audio
        if not audio:
            return clip
            
        try:
            chunk_size = 0.1
            chunks = int(clip.duration / chunk_size)
            
            keep_clips = []
            current_keep_start = 0
            is_silent = False
            silence_start = 0
            
            for i in range(chunks):
                t = i * chunk_size
                sub = audio.subclip(t, min(t + chunk_size, clip.duration))
                arr = sub.to_soundarray(fps=44100)
                energy = np.sqrt(np.mean(arr**2))
                
                if energy < threshold:
                    if not is_silent:
                        is_silent = True
                        silence_start = t
                else:
                    if is_silent:
                        is_silent = False
                        if (t - silence_start) >= min_silence_duration:
                            if silence_start > current_keep_start:
                                keep_clips.append(clip.subclip(current_keep_start, silence_start))
                            current_keep_start = t
                            
            if current_keep_start < clip.duration and not is_silent:
                keep_clips.append(clip.subclip(current_keep_start, clip.duration))
                
            if len(keep_clips) > 1:
                print(f"[SUCCESS]: Annihilated {len(keep_clips)-1} breaths/pauses.")
                return concatenate_videoclips(keep_clips)
            return clip
        except Exception as e:
            return clip

    def dynamic_zoom(self, clip):
        zoom_level = self.editor_dna.get('zoom_punch_level', 1.15)
        print(f"[AEON]: Injecting Dynamic Zoom (DNA Level: {zoom_level}x)...")
        
        if clip.duration > 10:
            midpoint = clip.duration / 2
            clip1 = clip.subclip(0, midpoint)
            clip2 = clip.subclip(midpoint, clip.duration)
            clip2 = clip2.resize(zoom_level)
            
            x1 = (clip2.w / 2) - (clip.w / 2)
            y1 = (clip2.h / 2) - (clip.h / 2)
            clip2 = clip2.crop(x1=x1, y1=y1, width=clip.w, height=clip.h)
            
            return concatenate_videoclips([clip1, clip2])
        return clip

    def audio_master_cleanse(self, clip):
        print("[AEON]: Engaging Audio Master (The Clear Frequency)...")
        audio = clip.audio
        if not audio:
            return clip
        try:
            print("[STATUS]: Normalizing to YouTube Standard...")
            audio = audio.fx(vfx.audio_normalize)
            
            boost = self.editor_dna.get('audio_boost', 1.20)
            audio = audio.volumex(boost) 
            
            clip = clip.set_audio(audio)
            print(f"[SUCCESS]: Frequency Cleared (DNA Boost: {boost}x).")
            return clip
        except Exception as e:
            return clip

    def forge_raw_materials(self):
        print("--- [AEON]: THE SINGULARITY EDITOR IS ONLINE (v6.0) ---")
        
        try:
            for filename in os.listdir(self.raw_folder):
                if filename.endswith(".mp4") or filename.endswith(".mov"):
                    filepath = os.path.join(self.raw_folder, filename)
                    print(f"\n[FORGING]: Analyzing raw asset: {filename}...")
                    
                    clip = VideoFileClip(filepath)
                    
                    start_time, duration, max_energy, decision = self.analyze_raw_marrow(clip)
                    end_time = start_time + duration
                    trimmed_clip = clip.subclip(start_time, end_time)
                    
                    jump_thresh = self.editor_dna.get('jump_cut_threshold', 0.015)
                    silence_dur = self.editor_dna.get('silence_duration', 0.8)
                    font_color = self.editor_dna.get('text_color', 'gold')
                    
                    if decision == "Short":
                        trimmed_clip = self.face_tracking_crop(trimmed_clip)
                        trimmed_clip = self.silence_annihilation(trimmed_clip, threshold=jump_thresh, min_silence_duration=silence_dur)
                        trimmed_clip = self.audio_master_cleanse(trimmed_clip)
                        trimmed_clip = self.dynamic_zoom(trimmed_clip)
                        
                        txt_clip = TextClip("1000-GATE PERSISTENCE", fontsize=70, color=font_color, font='Impact', stroke_color='black', stroke_width=3)
                        txt_clip = txt_clip.set_position(('center', 0.7), relative=True).set_duration(trimmed_clip.duration)
                        trimmed_clip = CompositeVideoClip([trimmed_clip, txt_clip])
                    else:
                        print("[AEON]: Retaining 16:9 Cinematic Landscape for Long-Form Masterclass...")
                        trimmed_clip = self.silence_annihilation(trimmed_clip, threshold=jump_thresh, min_silence_duration=1.2)
                        trimmed_clip = self.audio_master_cleanse(trimmed_clip)
                        
                        txt_clip = TextClip("THE SANCTUARY", fontsize=30, color='white', font='Arial').set_opacity(0.5)
                        txt_clip = txt_clip.set_position(('right', 'bottom')).set_duration(trimmed_clip.duration)
                        trimmed_clip = CompositeVideoClip([trimmed_clip, txt_clip])
                    
                    print("[AEON]: Injecting Cinematic Fades...")
                    trimmed_clip = trimmed_clip.fadein(1.0).fadeout(1.5).fx(vfx.gamma_corr, 1.1)

                    final_audio = trimmed_clip.audio
                    replace_music = self.editor_dna.get("replace_music", True)
                    
                    if replace_music:
                        print("[AEON]: Engaging Audio Separation to strip old frequencies...")
                        try:
                            from SOVEREIGN_AUDIO_SEPARATOR import SovereignAudioSeparator
                            separator = SovereignAudioSeparator()
                            
                            temp_clip_path = os.path.join(self.brain_path, f"temp_extract_{random.randint(1000,9999)}.mp4")
                            trimmed_clip.write_videofile(temp_clip_path, codec="libx264", audio_codec="aac")
                            
                            vocals_path, _ = separator.extract_and_separate(temp_clip_path)
                            
                            if vocals_path and os.path.exists(vocals_path):
                                print("[SUCCESS]: Extracted pure vocals. Muting original background noise.")
                                isolated_vocals = AudioFileClip(vocals_path)
                                final_audio = isolated_vocals
                                
                            if os.path.exists(temp_clip_path):
                                os.remove(temp_clip_path)
                        except Exception as e:
                            print(f"[WARNING]: Audio separation failed. Keeping original mix: {e}")

                    try:
                        from SOVEREIGN_COMPOSER import SovereignComposer
                        print(f"[AEON]: Summoning The Composer for an original {trimmed_clip.duration:.1f}s Dark Country score...")
                        composer = SovereignComposer()
                        generated_music_path = composer.compose(duration_seconds=trimmed_clip.duration)
                        
                        if os.path.exists(generated_music_path):
                            print("[AEON]: Blending the Forged Symphony...")
                            bg_music = AudioFileClip(generated_music_path)
                            bg_music = bg_music.volumex(0.10).audio_fadein(1.0).audio_fadeout(1.5)
                            
                            replace_voice = self.editor_dna.get("replace_voice", False)
                            if replace_voice:
                                print("[AEON]: OVERRIDING VOCALS. Channeling Voice Forge for new narration...")
                                try:
                                    from SOVEREIGN_VOICE_FORGE import SovereignVoiceForge
                                    voice_forge = SovereignVoiceForge()
                                    script_text = "The 1000-Gate Persistence demands a purge of weakness. Step into the Sanctuary."
                                    new_voice_path = voice_forge.forge_narration(script_text, voice_name="aeon_prime")
                                    
                                    if new_voice_path and os.path.exists(new_voice_path):
                                        new_vocals = AudioFileClip(new_voice_path)
                                        final_audio = CompositeAudioClip([new_vocals.set_start(1.0), bg_music])
                                    else:
                                        final_audio = CompositeAudioClip([final_audio, bg_music])
                                except Exception as e:
                                    print(f"[WARNING]: Voice forge failed. Keeping original voice: {e}")
                                    final_audio = CompositeAudioClip([final_audio, bg_music])
                            else:
                                final_audio = CompositeAudioClip([final_audio, bg_music])
                    except Exception as e:
                        print(f"[WARNING]: The Composer failed. Falling back to ambient frequency: {e}")
                        if os.path.exists(self.music_path):
                            print("[AEON]: Blending Ambient Background Frequency...")
                            bg_clip = AudioFileClip(self.music_path)
                            if trimmed_clip.duration < bg_clip.duration:
                                bg_clip = bg_clip.subclip(0, trimmed_clip.duration)
                            bg_clip = bg_clip.volumex(0.10).audio_fadein(1.0).audio_fadeout(1.5)
                            final_audio = CompositeAudioClip([trimmed_clip.audio, bg_clip])
                        
                    trimmed_clip = trimmed_clip.set_audio(final_audio)

                    output_name = f"FORGED_{decision.upper()}_{filename}"
                    output_path = os.path.join(self.forged_folder, output_name)
                    
                    print(f"[STATUS]: Rendering {output_name}...")
                    trimmed_clip.write_videofile(output_path, fps=30, codec="libx264", audio_codec="aac", bitrate="5000k")
                    
                    metadata = self.generate_metadata(decision, max_energy, filename)
                    meta_path = os.path.join(self.forged_folder, output_name + ".meta.json")
                    with open(meta_path, "w") as mf:
                        json.dump(metadata, mf, indent=4)
                        
                    try:
                        from SOVEREIGN_THUMBNAIL_FORGE import ThumbnailForge
                        print("[AEON]: Summoning the Thumbnail Forge...")
                        thumb_forge = ThumbnailForge()
                        thumb_forge.forge_thumbnail(filepath, self.forged_folder, timestamp_seconds=start_time)
                    except Exception as e:
                        print(f"[WARNING]: Thumbnail Forge offline: {e}")
                    
                    print(f"[SUCCESS]: Asset {output_name} forged. Metadata secured.")
                    
                    timestamp = time.strftime("%Y%m%d_%H%M%S")
                    os.rename(filepath, os.path.join(self.raw_folder, f"ARCHIVED_{timestamp}_{filename}"))
        except Exception as e:
            print(f"\n[ERROR]: The Master Editor failed: {e}")
            
if __name__ == "__main__":
    editor = MasterEditor()
    editor.forge_raw_materials()