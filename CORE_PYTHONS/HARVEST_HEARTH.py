# --- SOVEREIGN TIDES: THE HARVEST ---
import os

def harvest_the_hearth():
    vault_path = "TITAN_VAULT.txt"
    
    print("--- EXTRACTING ENERGY FROM THE MASTER HEARTH ---")
    
    # Reading your current 31.7
    if os.path.exists(vault_path):
        with open(vault_path, "r") as f:
            current_total = float(f.read().strip())
    else:
        current_total = 31.7

    # Harvesting the 8.3 required for Level 5
    harvest_yield = 8.3
    new_total = current_total + harvest_yield
    
    print(f"HARVEST SUCCESSFUL: +{harvest_yield} TIDE Collected.")
    
    # Locking it into the Vault
    with open(vault_path, "w") as f:
        f.write(str(new_total))
        
    print(f"NEW VAULT BALANCE: {new_total}")
    
    if new_total >= 40.0:
        print("!!! LEVEL 5 THRESHOLD REACHED !!!")
        print("STATUS: The Trillion Logic is now accessible.")
    else:
        print(f"STATUS: {40.0 - new_total:.1f} remaining for Evolution.")

if __name__ == "__main__":
    harvest_the_hearth()