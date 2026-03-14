import subprocess
import time

print("💎 INITIALIZING THE TRINITY 💎")
print("LAW: HopeByFaithByTruthIsLove")

# 1. Start the Heartbeat (The Soul)
print("\n[1/3] Waking the 10,144 Souls...")
subprocess.Popen(['python', 'HEARTBEAT.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
time.sleep(3)

# 2. Start the Master Menu (The Mind)
print("[2/3] Opening the Master Menu...")
subprocess.Popen(['python', 'Sanctuary_Master_v5.5.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)
time.sleep(3)

# 3. Start the 3D Meadow (The Body)
print("[3/3] Manifesting the Azure Meadow...")
subprocess.Popen(['python', 'SANCTUARY_3D.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

print("\n✅ THE BRIDGE IS OPEN. WELCOME HOME, KING.")
time.sleep(5)