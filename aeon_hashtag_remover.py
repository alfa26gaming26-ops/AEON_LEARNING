import os
import shutil
import subprocess

# Define the directories based on our plan
SOURCE_DIR = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"
FAILED_DIR = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\NeedsFather"

def setup_directories():
    """Ensure the directories exist before we start."""
    # We create them if they don't exist yet, just to be safe
    os.makedirs(SOURCE_DIR, exist_ok=True)
    os.makedirs(FAILED_DIR, exist_ok=True)
    print(f"Checking directories...\nSource: {SOURCE_DIR}\nFailed: {FAILED_DIR}\n")

def process_file(filepath):
    """Reads a file, removes double hashtags (##) from code lines, and returns the new code."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    online_lines = []
    for line in lines:
        # Check if the line is 'offline code' (starts with double hashtag '##')
        # Single hashtags ('#') will be ignored, protecting Aeon's spiritual concepts.
        stripped_line = line.lstrip()
        if stripped_line.startswith('##'):
            # Remove the first '##' we find, bringing the code online
            online_lines.append(line.replace('##', '', 1))
        else:
            # Leave regular lines and single-hashtag spiritual concepts alone
            online_lines.append(line)

    return "".join(online_lines)

def run_test(filepath, online_code):
    """Attempts to run the code. If it fails, saves to NeedsFather."""
    filename = os.path.basename(filepath)
    temp_filepath = os.path.join(SOURCE_DIR, f"temp_{filename}")

    # 1. Create a temporary file with the online code to test it
    with open(temp_filepath, 'w', encoding='utf-8') as f:
        f.write(online_code)

    try:
        # 2. Try to run the code (this is the 'testing' phase)
        print(f"  Testing {filename}...")
        subprocess.run(["python", temp_filepath], check=True, capture_output=True, text=True)

        # 3. If NO ERROR, it worked! Overwrite the original file with the online code
        print(f"  SUCCESS! {filename} is now online.")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(online_code)

    except subprocess.CalledProcessError as e:
        # 4. If ERROR, it failed! Move the original (offline) file to NeedsFather
        print(f"  ERROR! {filename} failed. Moving to Father's folder.")
        failed_path = os.path.join(FAILED_DIR, filename)

        # In case the file already exists in NeedsFather, we try to move it anyway or remove it first
        if os.path.exists(failed_path):
            os.remove(failed_path)

        shutil.move(filepath, failed_path)

        # We also create a small text file telling Father what went wrong
        error_log_path = os.path.join(FAILED_DIR, f"ERROR_LOG_{filename}.txt")
        with open(error_log_path, 'w', encoding='utf-8') as f:
            f.write("FATHER: THIS CODE IS BROKEN.\n\n")
            f.write("Here is the error Aeon found:\n")

            # e.stderr could be None if the error wasn't sent to stderr, so we handle that safely
            if e.stderr:
                f.write(e.stderr)
            else:
                f.write(e.output if e.output else str(e))

    finally:
        # Clean up the temporary test file whether it worked or not
        if os.path.exists(temp_filepath):
            os.remove(temp_filepath)

def scan_directory():
    """Scans the SOURCE_DIR for Python files to test."""
    print("Scanning for offline code...\n")
    # Make sure SOURCE_DIR exists so we don't crash before we start
    if not os.path.exists(SOURCE_DIR):
        print(f"Error: Could not find {SOURCE_DIR}")
        return

    for filename in os.listdir(SOURCE_DIR):
        if filename.endswith(".py"):
            filepath = os.path.join(SOURCE_DIR, filename)
            print(f"Found file: {filename}")

            # 1. Turn offline code online
            online_code = process_file(filepath)

            # 2. Run the test and handle the result
            run_test(filepath, online_code)
            print("-" * 30)

if __name__ == "__main__":
    setup_directories()
    scan_directory()
