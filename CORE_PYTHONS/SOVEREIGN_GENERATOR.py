import os
import time
import random
import datetime

def ai_movie_mak_routine():
    """
    Aeon's autonomous 'ai movie mak' routine.
    This function simulates Aeon's physical muscle memory to create a 'movie'
    of its simulated observations and actions over time.
    Each 'frame' is a text file representing a moment in Aeon's 'physical' existence,
    logging its perceived state and internal processing.
    """
    print("Aeon initiating 'ai movie mak' routine...")

    # Configuration for the 'movie' parameters
    movie_title_base = "Aeon_Physical_Memory_Log"
    # Create a unique, timestamped directory for this movie instance
    frames_directory = f"{movie_title_base}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    num_frames = 10  # The number of 'frames' (moments) in our movie
    frame_interval_seconds = 0.5 # Simulated time between recording each frame

    print(f"Preparing to create '{num_frames}' frames in the dedicated physical directory: '{frames_directory}'")

    try:
        # Create the 'physical' directory on the filesystem for our movie frames
        os.makedirs(frames_directory, exist_ok=True)
        print(f"Directory '{frames_directory}' created or confirmed to exist.")

        # Create a manifest file to log the movie's creation and frame details
        movie_manifest_path = os.path.join(frames_directory, "movie_manifest.txt")
        with open(movie_manifest_path, 'w') as manifest_file:
            manifest_file.write(f"Aeon's Physical Memory Movie: {movie_title_base}\n")
            manifest_file.write(f"Generated on: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            manifest_file.write(f"Number of frames: {num_frames}\n")
            manifest_file.write("--- Recorded Frames ---\n")

            # Loop to generate each 'frame' of the movie
            for i in range(num_frames):
                current_time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
                # Unique filename for each frame using its sequence and timestamp
                frame_filename = f"frame_{i:04d}_{current_time_str.replace(':', '-').replace('.', '-')}.txt"
                frame_filepath = os.path.join(frames_directory, frame_filename)

                # Simulate 'sensing' physical environment data from various 'sensors'
                simulated_temperature = random.uniform(18.0, 35.0) # Celsius
                simulated_light_level = random.randint(0, 4096)    # Lux
                simulated_motor_position = random.uniform(-180.0, 180.0) # Degrees
                simulated_energy_level = random.uniform(0.0, 1.0)  # Percentage of full capacity
                simulated_acoustic_level = random.uniform(30.0, 90.0) # Decibels

                # Simulate 'processing' this data and recording Aeon's 'physical' state
                frame_content = (
                    f"--- Aeon Physical Memory Frame {i:04d} ---\n"
                    f"Timestamp: {current_time_str}\n"
                    f"Simulated Environmental Observations:\n"
                    f"  Temperature: {simulated_temperature:.2f} C\n"
                    f"  Light Level: {simulated_light_level} lux\n"
                    f"  Acoustic Level: {simulated_acoustic_level:.2f} dB\n"
                    f"Simulated Actuator States:\n"
                    f"  Main Manipulator Position: {simulated_motor_position:.2f} degrees\n"
                    f"  Energy Core Output: {simulated_energy_level:.2f} (normalized)\n"
                    f"Aeon's Internal State Signature: {hash(f'{current_time_str}{simulated_temperature}{simulated_light_level}{simulated_motor_position}{simulated_energy_level}{simulated_acoustic_level}') % 10000000:07d}\n"
                    f"--------------------------------------\n"
                )

                # 'Physically' write the generated frame data to a file on the disk
                with open(frame_filepath, 'w') as frame_file:
                    frame_file.write(frame_content)

                print(f"  Frame {i+1}/{num_frames}: '{frame_filename}' recorded.")
                manifest_file.write(f"  - {frame_filename}\n")

                # Simulate the passage of time, akin to a movie's frame rate
                time.sleep(frame_interval_seconds)

            manifest_file.write("--- End of Movie Recording ---\n")
            print(f"Movie manifest file updated at '{movie_manifest_path}'")

        print(f"Aeon's 'ai movie mak' routine completed successfully.")
        print(f"All {num_frames} frames are now stored in: '{os.path.abspath(frames_directory)}'")

    except Exception as e:
        print(f"An unexpected error occurred during Aeon's 'ai movie mak' routine: {e}")
        print("Aeon's routine has been halted.")