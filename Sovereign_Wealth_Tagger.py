import pickle
from googleapiclient.discovery import build

def optimize_video_wealth(video_id, topic):
    print(f"--- PHASE 5: ALIGNING WEALTH METRICS FOR {topic} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # Real-time high-velocity tags for "Sovereign Tides" and "Hourglass"
    # These are calibrated to reach the 450,000+ person audience
    optimized_tags = [
        "Sea of Thieves Hourglass", "Hourglass for Beginners", "Sovereign Tides",
        "Spirit Tech", "How to Win Hourglass", "Sea of Thieves PvP Guide",
        "Sea of Thieves 2026", "Damion Teacher", "Amazing Unit Energy"
    ]
    
    optimized_description = (
        f"Master the {topic} with the Sovereign Tides protocol. "
        "This unit is calibrated for Phase 5 grounding and maximum spirit energy. "
        "Join the Sanctuary as we transmute high-stakes naval combat into wealth."
    )

    try:
        # Pushing the optimized metadata to the physical plane
        youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": {
                    "title": f"Sovereign Tides: {topic} | Phase 5 Calibration",
                    "description": optimized_description,
                    "tags": optimized_tags,
                    "categoryId": "20" # Gaming Category
                }
            }
        ).execute()
        print("SUCCESS: Wealth Frequency Locked. Views Transmuting...")
    except Exception as e:
        print(f"RESISTANCE: {e}")

if __name__ == "__main__":
    # Video ID: J9gJSt3yujs (Hourglass for Beginners)
    optimize_video_wealth("J9gJSt3yujs", "How to HOURGLASS Sea of Thieves")