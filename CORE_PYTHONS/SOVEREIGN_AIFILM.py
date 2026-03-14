import time
import random
import os
import shutil

class Config:
    OUTPUT_DIR = "aeon_production_log"
    FRAME_RATE = 24
    DEFAULT_FOCUS_DISTANCE = 1.5
    DEFAULT_ZOOM_LEVEL = 1.0
    DEFAULT_LIGHT_INTENSITY = 0.8
    ROBOT_ARM_SPEED_FACTOR = 0.05
    CAMERA_CAPTURE_DELAY = 0.1

def _simulate_physical_delay(duration):
    time.sleep(duration)

def _prepare_output_directory():
    if not os.path.exists(Config.OUTPUT_DIR):
        os.makedirs(Config.OUTPUT_DIR)
    else:
        for item in os.listdir(Config.OUTPUT_DIR):
            item_path = os.path.join(Config.OUTPUT_DIR, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

class RobotArm:
    def __init__(self, identifier="AeonArm"):
        self.identifier = identifier
        self.current_position = [0.0, 0.0, 0.0]
        self.gripper_status = "open"
        self.held_object = None
        self.mounted_camera = None

    def move_effector_to(self, target_coordinates):
        print(f"{self.identifier}: Initiating movement from {self.current_position} to {target_coordinates}.")
        distance_travelled = ((target_coordinates[0] - self.current_position[0])**2 +
                              (target_coordinates[1] - self.current_position[1])**2 +
                              (target_coordinates[2] - self.current_position[2])**2)**0.5
        _simulate_physical_delay(distance_travelled * Config.ROBOT_ARM_SPEED_FACTOR)
        self.current_position = target_coordinates
        print(f"{self.identifier}: Effector reached {self.current_position}.")
        return {"action": "move_effector_to", "target": target_coordinates, "final_position": self.current_position}

    def control_gripper(self, command, obj=None):
        if command not in ["open", "close"]:
            raise ValueError("Gripper command must be 'open' or 'close'.")
        print(f"{self.identifier}: Executing gripper command: '{command}'.")
        _simulate_physical_delay(0.5)
        if command == "close":
            self.gripper_status = "holding"
            self.held_object = obj
            print(f"{self.identifier}: Gripper secured. Holding: {obj.name if obj else 'nothing'}.")
        else:
            self.gripper_status = "open"
            if self.held_object:
                print(f"{self.identifier}: Releasing {self.held_object.name}.")
                self.held_object = None
            else:
                print(f"{self.identifier}: Gripper opened.")
        return {"action": "control_gripper", "state": self.gripper_status, "object": obj.name if obj else None}

    def attach_camera(self, camera_unit):
        self.mounted_camera = camera_unit
        print(f"{self.identifier}: Camera '{camera_unit.identifier}' attached.")
        return {"action": "attach_camera", "camera": camera_unit.identifier}

    def get_camera_location(self):
        return self.current_position

class CameraUnit:
    def __init__(self, identifier="AeonCam"):
        self.identifier = identifier
        self.focus_distance = Config.DEFAULT_FOCUS_DISTANCE
        self.zoom_level = Config.DEFAULT_ZOOM_LEVEL
        self.power_state = False
        self.frame_index = 0

    def power_toggle(self, state):
        self.power_state = state
        print(f"{self.identifier}: Power {'ON' if self.power_state else 'OFF'}.")
        return {"action": "power_toggle", "state": self.power_state}

    def adjust_focus(self, distance):
        if not self.power_state:
            print(f"{self.identifier}: Cannot adjust focus, unit is OFF.")
            return None
        self.focus_distance = max(0.1, distance)
        print(f"{self.identifier}: Focus set to {self.focus_distance:.2f}m.")
        _simulate_physical_delay(0.1)
        return {"action": "adjust_focus", "distance": self.focus_distance}

    def adjust_zoom(self, level):
        if not self.power_state:
            print(f"{self.identifier}: Cannot adjust zoom, unit is OFF.")
            return None
        self.zoom_level = max(0.1, level)
        print(f"{self.identifier}: Zoom set to {self.zoom_level:.2f}x.")
        _simulate_physical_delay(0.1)
        return {"action": "adjust_zoom", "level": self.zoom_level}

    def capture_still_frame(self, scene_context=""):
        if not self.power_state:
            print(f"{self.identifier}: Cannot capture, unit is OFF.")
            return None
        _simulate_physical_delay(Config.CAMERA_CAPTURE_DELAY)
        self.frame_index += 1
        filename = os.path.join(Config.OUTPUT_DIR, f"frame_{self.frame_index:05d}.jpg")
        with open(filename, 'w') as f:
            f.write(f"Aeon Frame {self.frame_index}\n")
            f.write(f"Context: {scene_context}\n")
            f.write(f"Focus: {self.focus_distance:.2f}m, Zoom: {self.zoom_level:.2f}x\n")
            f.write(f"Timestamp: {time.time()}\n")
        print(f"{self.identifier}: Captured '{filename}'.")
        return {"action": "capture_still_frame", "filename": filename, "frame_number": self.frame_index}

class LightingSystem:
    def __init__(self, identifier="AeonLight"):
        self.identifier = identifier
        self.intensity = Config.DEFAULT_LIGHT_INTENSITY
        self.color_temperature = 5500

    def set_intensity(self, level):
        self.intensity = max(0.0, min(1.0, level))
        print(f"{self.identifier}: Intensity adjusted to {self.intensity:.2f}.")
        _simulate_physical_delay(0.05)
        return {"action": "set_intensity", "level": self.intensity}

    def set_color_temperature(self, kelvin_value):
        self.color_temperature = max(2000, min(10000, kelvin_value))
        print(f"{self.identifier}: Color temperature set to {self.color_temperature}K.")
        _simulate_physical_delay(0.05)
        return {"action": "set_color_temperature", "kelvin": self.color_temperature}

class PhysicalObject:
    def __init__(self, name_tag, initial_coordinates=[0.0, 0.0, 0.0]):
        self.name = name_tag
        self.coordinates = initial_coordinates
        print(f"SceneObject: '{self.name_tag}' instantiated at {self.coordinates}.")

    def relocate(self, new_coordinates):
        print(f"SceneObject: '{self.name}' moved to {new_coordinates}.")
        self.coordinates = new_coordinates
        return {"action": "object_relocate", "object": self.name, "new_coordinates": self.coordinates}

class RotationalPlatform:
    def __init__(self, identifier="AeonTurntable"):
        self.identifier = identifier
        self.current_angle = 0.0
        self.object_present = None

    def place_item(self, item_obj):
        self.object_present = item_obj
        print(f"{self.identifier}: '{item_obj.name}' positioned on platform.")
        return {"action": "place_item_on_platform", "object": item_obj.name}

    def rotate_to_angle(self, angle_degrees):
        print(f"{self.identifier}: Rotating from {self.current_angle:.1f} to {angle_degrees:.1f} degrees.")
        _simulate_physical_delay(abs(angle_degrees - self.current_angle) / 90.0)
        self.current_angle = angle_degrees % 360
        print(f"{self.identifier}: Rotated to {self.current_angle:.1f} degrees.")
        return {"action": "rotate_platform", "angle": self.current_angle}

class AeonMovieMaker:
    def __init__(self, ai_name="Aeon"):
        self.ai_name = ai_name
        self.robot_arm = RobotArm("AeonArm")
        self.camera_unit = CameraUnit("AeonCam")
        self.lighting_system = LightingSystem("AeonLight")
        self.rotational_platform = RotationalPlatform("AeonTurntable")
        self.robot_arm.attach_camera(self.camera_unit)

        self.action_memory = []
        self.active_sequence_name = None
        self.recording_active = False

        print(f"{self.ai_name}: AI Movie Maker system initializing.")

    def _record_action(self, action_data):
        if self.recording_active and self.active_sequence_name:
            self.action_memory[-1]["actions"].append(action_data)

    def initiate_sequence_recording(self, sequence_label):
        if self.recording_active:
            print(f"{self.ai_name}: Recording already active. Terminate current sequence first.")
            return
        self.active_sequence_name = sequence_label
        self.action_memory.append({"name": sequence_label, "actions": []})
        self.recording_active = True
        print(f"{self.ai_name}: Recording sequence '{sequence_label}' initiated.")

    def terminate_sequence_recording(self):
        if not self.recording_active:
            print(f"{self.ai_name}: No active recording to terminate.")
            return
        self.recording_active = False
        print(f"{self.ai_name}: Recording sequence '{self.active_sequence_name}' terminated.")
        self.active_sequence_name = None

    def execute_from_memory(self, sequence_label):
        print(f"{self.ai_name}: Recalling and executing sequence: '{sequence_label}'...")
        sequence_found = False
        for seq in self.action_memory:
            if seq["name"] == sequence_label:
                sequence_found = True
                for action in seq["actions"]:
                    action_type = action["action"]
                    if action_type == "move_effector_to":
                        self.robot_arm.move_effector_to(action["target"])
                    elif action_type == "control_gripper":
                        obj_name = action.get("object")
                        obj = PhysicalObject(obj_name) if obj_name else None
                        self.robot_arm.control_gripper(action["state"], obj)
                    elif action_type == "power_toggle":
                        self.camera_unit.power_toggle(action["state"])
                    elif action_type == "adjust_focus":
                        self.camera_unit.adjust_focus(action["distance"])
                    elif action_type == "adjust_zoom":
                        self.camera_unit.adjust_zoom(action["level"])
                    elif action_type == "capture_still_frame":
                        self.camera_unit.capture_still_frame(f"Memory Playback of '{sequence_label}'")
                    elif action_type == "set_intensity":
                        self.lighting_system.set_intensity(action["level"])
                    elif action_type == "set_color_temperature":
                        self.lighting_system.set_color_temperature(action["kelvin"])
                    elif action_type == "place_item_on_platform":
                        obj = PhysicalObject(action["object"])
                        self.rotational_platform.place_item(obj)
                    elif action_type == "rotate_platform":
                        self.rotational_platform.rotate_to_angle(action["angle"])
                    else:
                        print(f"{self.ai_name}: Unrecognized action during playback: {action_type}")
                break
        if not sequence_found:
            print(f"{self.ai_name}: Sequence '{sequence_label}' not found in memory.")
        print(f"{self.ai_name}: Sequence '{sequence_label}' execution complete.")

    def _assess_shot_quality(self):
        quality_score = random.uniform(0.5, 1.0)
        print(f"{self.ai_name}: Assessing shot quality: {quality_score:.2f} (1.0 is optimal).")

        evaluation_feedback = {}
        if quality_score < 0.7:
            evaluation_feedback["refocus_advised"] = True
            evaluation_feedback["lighting_adjustment_advised"] = True
            print(f"{self.ai_name}: Shot requires refinement: focus and lighting deviations detected.")
        else:
            print(f"{self.ai_name}: Shot quality deemed satisfactory.")
        return evaluation_feedback

    def _adapt_parameters_based_on_feedback(self, feedback_data):
        if feedback_data.get("refocus_advised"):
            new_focus_setting = self.camera_unit.focus_distance + random.uniform(-0.1, 0.1)
            self.camera_unit.adjust_focus(new_focus_setting)
            self._record_action({"action": "adjust_focus", "distance": self.camera_unit.focus_distance})
        if feedback_data.get("lighting_adjustment_advised"):
            new_intensity_setting = self.lighting_system.intensity + random.uniform(-0.1, 0.1)
            self.lighting_system.set_intensity(new_intensity_setting)
            self._record_action({"action": "set_intensity", "level": self.lighting_system.intensity})

    def produce_movie(self, film_title="AutonomousProduction", scene_count=2, shots_per_scene=3):
        print(f"{self.ai_name}: Commencing movie production: '{film_title}'.")
        _prepare_output_directory()
        self.camera_unit.power_toggle(True)
        self._record_action(self.camera_unit.power_toggle(True))

        primary_subject = PhysicalObject("ProductModel", initial_coordinates=[0.0, 0.0, 0.1])
        self.rotational_platform.place_item(primary_subject)
        self._record_action(self.rotational_platform.place_item(primary_subject))

        self.initiate_sequence_recording(f"{film_title}_full_production")

        for scene_index in range(scene_count):
            print(f"\n{self.ai_name}: --- Scene {scene_index + 1} ---")
            
            target_arm_location = [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), random.uniform(0.2, 0.8)]
            self.robot_arm.move_effector_to(target_arm_location)
            self._record_action(self.robot_arm.move_effector_to(target_arm_location))

            self.lighting_system.set_intensity(random.uniform(0.6, 0.9))
            self._record_action(self.lighting_system.set_intensity(self.lighting_system.intensity))
            self.lighting_system.set_color_temperature(random.choice([3200, 4500, 5500, 6500]))
            self._record_action(self.lighting_system.set_color_temperature(self.lighting_system.color_temperature))

            for shot_index in range(shots_per_scene):
                print(f"{self.ai_name}: Capturing Shot {shot_index + 1} for Scene {scene_index + 1}...")

                self.camera_unit.adjust_focus(random.uniform(1.0, 2.0))
                self._record_action(self.camera_unit.adjust_focus(self.camera_unit.focus_distance))
                self.camera_unit.adjust_zoom(random.uniform(0.8, 1.5))
                self._record_action(self.camera_unit.adjust_zoom(self.camera_unit.zoom_level))
                self.rotational_platform.rotate_to_angle(random.uniform(0, 360))
                self._record_action(self.rotational_platform.rotate_to_angle(self.rotational_platform.current_angle))

                capture_feedback = self.camera_unit.capture_still_frame(f"Scene {scene_index+1}, Shot {shot_index+1}")
                self._record_action(capture_feedback)
                
                evaluation_results = self._assess_shot_quality()
                if evaluation_results.get("refocus_advised") or evaluation_results.get("lighting_adjustment_advised"):
                    print(f"{self.ai_name}: Retaking Shot {shot_index + 1} due to quality assessment.")
                    self._adapt_parameters_based_on_feedback(evaluation_results)
                    retake_feedback = self.camera_unit.capture_still_frame(f"Scene {scene_index+1}, Shot {shot_index+1} (Retake)")
                    self._record_action(retake_feedback)

        self.terminate_sequence_recording()
        self.camera_unit.power_toggle(False)
        self._record_action(self.camera_unit.power_toggle(False))
        print(f"\n{self.ai_name}: Movie '{film_title}' production completed. Output in '{Config.OUTPUT_DIR}'.")
        print(f"{self.ai_name}: Total frames captured: {self.camera_unit.frame_index}.")
        print(f"{self.ai_name}: Full production sequence saved as '{film_title}_full_production' in muscle memory.")

def ai_movie_maker_script():
    aeon_system = AeonMovieMaker("Aeon")
    aeon_system.produce_movie(film_title="FatherProjectShowcase", scene_count=3, shots_per_scene=4)

    print("\n" * 3)
    print("--------------------------------------------------")
    print("AEON: DEMONSTRATING PHYSICAL MUSCLE MEMORY PLAYBACK")
    print("--------------------------------------------------")
    
    if os.path.exists(Config.OUTPUT_DIR):
        shutil.rmtree(Config.OUTPUT_DIR)
    _prepare_output_directory()
    
    aeon_system.camera_unit.frame_index = 0

    aeon_system.execute_from_memory("FatherProjectShowcase_full_production")

if __name__ == '__main__':
    ai_movie_maker_script()