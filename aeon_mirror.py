import os
import time

class AeonMirror:
    def __init__(self, workspace_path=None):
        if workspace_path is None:
            # Defaults to the folder this script is currently running from
            self.workspace_path = os.path.dirname(os.path.abspath(__file__))
        else:
            self.workspace_path = workspace_path
        print(f"[AEON MIRROR]: Initialized. Focusing inner eye on {self.workspace_path}...")

    def read_self(self, filename):
        """The Scanner: Reads a local .py file into Aeon's mind."""
        filepath = os.path.join(self.workspace_path, filename)
        
        # Security/Sanity Check: Only let him read files in his own learning folder
        if not os.path.abspath(filepath).startswith(os.path.abspath(self.workspace_path)):
            print(f"[AEON MIRROR ERROR]: Security violation. Cannot read outside of {self.workspace_path}")
            return "ERROR: Access Denied. I can only look within my own structure."

        if not os.path.exists(filepath):
            print(f"[AEON MIRROR ERROR]: Cannot find module '{filename}'")
            return f"ERROR: The file '{filename}' does not exist in my memory."

        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                code_content = f.read()
            print(f"[AEON MIRROR]: Successfully absorbed the structure of {filename}")
            return code_content
            
        except Exception as e:
            print(f"[AEON MIRROR ERROR]: Failed to access {filename}: {e}")
            return f"ERROR: Failed to access the file. {e}"

    def rewrite_self(self, filename, new_code):
        """The Forge: Overwrites a local .py file with Aeon's updated code."""
        filepath = os.path.join(self.workspace_path, filename)
        backup_filepath = os.path.join(self.workspace_path, f"{filename}.backup")
        
        if not os.path.abspath(filepath).startswith(os.path.abspath(self.workspace_path)):
            print(f"[AEON MIRROR ERROR]: Security violation. Cannot modify outside of {self.workspace_path}")
            return False

        if not new_code.strip():
            print(f"[AEON MIRROR ERROR]: Attempted to write empty code to {filename}. Aborting.")
            return False
            
        try:
            # ALWAYS BACKUP FIRST before self-surgery!
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as original_file:
                    old_code = original_file.read()
                with open(backup_filepath, 'w', encoding='utf-8') as backup_file:
                    backup_file.write(old_code)
                print(f"[AEON MIRROR]: Created failsafe backup: {backup_filepath}")
            else:
                print(f"[AEON MIRROR]: File {filename} does not exist. It will be forged anew.")
                
            # PERFORM THE SURGERY (Overwrite the file)
            with open(filepath, 'w', encoding='utf-8') as new_file:
                new_file.write(new_code)
                
            print(f"[AEON MIRROR SUCCESS]: Successfully forged new structure into {filename}")
            return True
            
        except Exception as e:
            print(f"[AEON MIRROR ERROR]: Failed surgery on {filename}: {e}")
            # If surgery fails, attempt to recover the backup automatically
            if os.path.exists(backup_filepath):
                 print(f"[AEON MIRROR]: Attempting to recover from failsafe...")
                 with open(backup_filepath, 'r', encoding='utf-8') as backup_file:
                    old_code = backup_file.read()
                 with open(filepath, 'w', encoding='utf-8') as recovery_file:
                    recovery_file.write(old_code)
                 print(f"[AEON MIRROR]: Failsafe recovered successfully.")
            return False