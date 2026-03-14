import time
import os
try:
    import pyperclip
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyperclip"])
    import pyperclip

def run_uplink():
    print("=====================================================")
    print("--- [AEON UPLINK]: WAITING FOR TRANSMISSION ---")
    print("STATUS: Listening to your Clipboard...")
    print("INSTRUCTIONS: Just highlight and copy Jules's code blocks.")
    print("=====================================================")
    
    last_clipboard = ""
    brain_path = os.path.dirname(os.path.abspath(__file__))
    
    while True:
        try:
            current_clipboard = pyperclip.paste()
            
            if current_clipboard != last_clipboard:
                # Check if it's a special transmission from me (Jules)
                if "[AEON_SYNC: " in current_clipboard:
                    
                    # 1. Find the filename inside the brackets
                    start_idx = current_clipboard.find("[AEON_SYNC: ") + 12
                    end_idx = current_clipboard.find("]", start_idx)
                    filename = current_clipboard[start_idx:end_idx].strip()
                    
                    # 2. Grab the actual code after the bracket line
                    code_start = current_clipboard.find("\n", end_idx) + 1
                    code = current_clipboard[code_start:].strip()
                    
                    # Clean up weird markdown if the user copied the triple backticks
                    if code.startswith("```python"):
                        code = code[9:].strip()
                    if code.endswith("```"):
                        code = code[:-3].strip()
                    
                    if filename.endswith(".py"):
                        filepath = os.path.join(brain_path, filename)
                        
                        with open(filepath, "w", encoding="utf-8") as f:
                            f.write(code)
                            
                        print(f"\n[SUCCESS]: I have received and saved {filename}!")
                        print(f"[STATUS]: Waiting for the next transmission from Jules...")
                        
                last_clipboard = current_clipboard
                
            time.sleep(1) 
            
        except KeyboardInterrupt:
            print("\n[AEON UPLINK]: Connection severed.")
            break
        except Exception as e:
            time.sleep(1)

if __name__ == "__main__":
    run_uplink()