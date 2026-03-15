import os
import subprocess
import shutil

def process_scripts(directory):
    needs_father_dir = os.path.join(directory, "NeedsFather")
    if not os.path.exists(needs_father_dir):
        os.makedirs(needs_father_dir)

    for filename in os.listdir(directory):
        if not filename.endswith(".py"):
            continue

        # Skip self and temporary testing files
        if filename == "aeon_hashtag_remover.py" or filename.startswith("temp_"):
            continue

        filepath = os.path.join(directory, filename)

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            continue

        if "##" not in content:
            continue

        print(f"Processing: {filename}")

        # Uncomment offline code without destroying indentation
        new_lines = []
        for line in content.splitlines():
            # If the line starts with ## (ignoring leading whitespace)
            if line.lstrip().startswith("##"):
                # Replace the first occurrence of ## with nothing, preserving leading space
                new_line = line.replace("##", "", 1)
                new_lines.append(new_line)
            else:
                new_lines.append(line)

        new_content = "\n".join(new_lines) + "\n"

        # Create a temporary file to test
        temp_filepath = os.path.join(directory, f"temp_{filename}")
        with open(temp_filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        # Test the script with a 15-second timeout (for infinite heartbeat loops)
        try:
            print(f"  -> Testing {filename}...")
            result = subprocess.run(
                ["python", temp_filepath],
                capture_output=True,
                text=True,
                timeout=15
            )

            if result.returncode == 0:
                print(f"  -> SUCCESS! Replacing original.")
                os.replace(temp_filepath, filepath)
            else:
                print(f"  -> FAILED! Moving to NeedsFather.")
                # Create an error log
                log_filepath = os.path.join(needs_father_dir, f"{filename}.log")
                with open(log_filepath, 'w', encoding='utf-8') as f:
                    f.write(result.stderr)
                # Move the failed script
                failed_filepath = os.path.join(needs_father_dir, filename)
                shutil.move(filepath, failed_filepath)
                # Clean up temp
                if os.path.exists(temp_filepath):
                    os.remove(temp_filepath)

        except subprocess.TimeoutExpired:
            print(f"  -> SUCCESS (Timeout - Infinite Loop). Replacing original.")
            os.replace(temp_filepath, filepath)
        except Exception as e:
            print(f"  -> SYSTEM ERROR testing {filename}: {e}")
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)

if __name__ == "__main__":
    target_directory = r"G:\My Drive\THE_SANCTUARY_OFFLINE\AEON_LEARNING\CORE_PYTHONS"
    # For safety in this environment, default to current dir if G: doesn't exist
    if not os.path.exists(target_directory):
        target_directory = "."

    print(f"Starting scan on: {target_directory}")
    process_scripts(target_directory)
    print("Scan complete.")
