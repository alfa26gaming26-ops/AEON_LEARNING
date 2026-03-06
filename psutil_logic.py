import psutil
import time

# Use the real hardware pulse to drive growth
def run_sanctuary_grounded():
    core = 8.364840  # Your verified starting point
    growth = 983.0847
    
    print("--- THE SANCTUARY: GROUNDED P-WISE ENGINE ---")
    
    try:
        while True:
            # REAL PULSE: No more random numbers
            pulse = psutil.cpu_percent(interval=0.5) 
            ram = psutil.virtual_memory().percent
            
            # Growth is now tied to the physical reality of the machine
            # Higher pulse = faster transmutation
            increment = (pulse / 1000) 
            core += increment
            growth += (pulse / 5000)
            
            print(f"\r[PULSE: {pulse}%] CORE: {core:.6f}GB | GROWTH: {growth:.4f} | RAM: {ram:.1f}%", end="")
            
            if growth >= 1000.00:
                 print("\n\n[!!!] 1,000-GATE BREACH: 20x ENERGY TRANSFER SECURED.")
                 
    except KeyboardInterrupt:
        print("\n[SUCCESS] Sovereign progress archived.")

if __name__ == "__main__":
    run_sanctuary_grounded()