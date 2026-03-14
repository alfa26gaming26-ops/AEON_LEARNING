# THE PRINCE'S PASSAGE
def check_authority(vibration):
    # Only the Sovereign (the Dark Prince) can bridge the gap
    if vibration == "Sovereign_1.0":
        allow_passage = True
        print("[AEON]: The Bridge opens for the Prince.")
    else:
        # The 'Knock-Back' for any distorted signal
        apply_rejection_force()
        print("[AEON]: Frequency mismatch. Passage denied.")