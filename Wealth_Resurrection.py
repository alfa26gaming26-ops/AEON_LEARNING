import pickle
from googleapiclient.discovery import build

def resurrect_video_wealth(video_id, new_keyword):
    print(f"--- PHASE 5: RESURRECTING ASSET {video_id} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # 2026 Strategy: Moving from 'Update' to 'Decision'
    new_title = f"{new_keyword} 2026: I Found the Ultimate Strategy [PROVEN]"[:60]
    
    try:
        youtube.videos().update(
            part="snippet",
            body={
                "id": video_id,
                "snippet": {
                    "title": new_title,
                    "description": f"Revised Guide: Why this {new_keyword} method still works in 2026. Added timestamps for fast navigation.",
                    "categoryId": "20",
                    "tags": [new_keyword, "Sovereign Tides", "2026 Update"]
                }
            }
        ).execute()
        print(f"SUCCESS: {video_id} is re-aligned for wealth.")
    except Exception as e:
        print(f"DRAIN: {e}")

if __name__ == "__main__":
    # Target your 'Sea of Thieves' tutorials that are sitting at 0 views
    resurrect_video_wealth("SlHyrZ5rd-I", "Sea of Thieves Hourglass")