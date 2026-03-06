import pickle
from googleapiclient.discovery import build

def boost_existing_wealth(video_id, target_niche):
    print(f"--- PHASE 5: RESURRECTING ASSET {video_id} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # 2026 Strategy: From 'Gaming' to 'Educational/Challenge'
    optimized_title = f"The {target_niche} Secret Nobody Tells You (2026 Update)"[:100]
    
    try:
        youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": {
                    "title": optimized_title,
                    "description": "0:00 Intro\n1:15 The Secret Method\n3:45 Real-time Results\n\nOptimized for 2026 Search Patterns.",
                    "tags": [target_niche, "Sovereign Tides", "Guide"],
                    "categoryId": "20"
                }
            }
        ).execute()
        print("SUCCESS: Frequency Aligned. View-Gate Open.")
    except Exception as e:
        print(f"RESISTANCE: {e}")

if __name__ == "__main__":
    # Apply to your existing Sea of Thieves assets
    boost_existing_wealth("SlHyrZ5rd-I", "Sea of Thieves Solo Strategy")