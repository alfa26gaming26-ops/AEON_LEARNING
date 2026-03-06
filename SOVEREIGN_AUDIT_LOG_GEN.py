import os

def run_logged_audit():
    sovereign_files = [f for f in os.listdir() if "SOVEREIGN_" in f]
    
    # Calculating Metrics
    heavy_marrow = 0
    shells = 0
    for f in sovereign_files:
        if os.path.getsize(f) > 400:
            heavy_marrow += 1
        else:
            shells += 1
            
    # Writing the Hard Copy
    with open("SANCTUARY_AUDIT_REPORT.txt", "w") as log:
        log.write("--- [AEON]: SYSTEM AUDIT REPORT ---\n")
        log.write(f"Total Sovereign Pillars: {len(sovereign_files)}\n")
        log.write(f"Heavy Marrow Units: {heavy_marrow}\n")
        log.write(f"Structural Shells: {shells}\n")
        log.write("----------------------------------\n")
        log.write("List of Pillars Standing:\n")
        for f in sorted(sovereign_files):
            log.write(f"{f}\n")

    print("[SUCCESS]: Audit Complete. Open SANCTUARY_AUDIT_REPORT.txt")

if __name__ == "__main__":
    run_logged_audit()