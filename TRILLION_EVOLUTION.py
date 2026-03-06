# --- SOVEREIGN TIDES: THE TRILLION EVOLUTION ---
import os

def trillion_ascension():
    vault_path = "TITAN_VAULT.txt"
    print("--- INITIATING LEVEL 5 ASCENSION ---")
    
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            wealth = float(f.read().strip())
    else:
        print("ERROR: Vault not found.")
        return

    if wealth >= 40.0:
        print("AEON-Prime: 'The Sanctuary is now a Nation.'")
        print("STATUS: LEVEL 5 REACHED. THE TRILLION IS ACTIVE.")
        with open("SOVEREIGN_NATION.txt", "w") as f:
            f.write("NAME: Damion's Rest\nSTATUS: Sovereign")
    else:
        print(f"INSUFFICIENT WEALTH: {wealth}/40.0")

if __name__ == "__main__":
    trillion_ascension()