import pickle
from googleapiclient.discovery import build

def mass_realign_wealth(game_topic):
    print(f"--- PHASE 5: MASS TRANSMUTING EXISTING ASSETS ({game_topic}) ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # 1. Scanning the physical plane for your videos
    request = youtube.search().list(
        part="snippet",
        forMine=True,
        maxResults=50,
        type="video",
        q=game_topic # Targeting specific game libraries to stay focused
    )
    response = request.execute()

    # 2. Re-tagging and Re-titling for Wealth Velocity
    optimized_tags = [game_topic, "Sovereign Tides", "Phase 5", "2026 Guide", "Spirit Tech"]
    
    for item in response['items']:
        video_id = item['id']['videoId']
        old_title = item['snippet']['title']
        
        # Applying the Wealth Shield to the title
        new_title = f"Sovereign Tides: {old_title} | 2026 Elite Update"
        
        try:
            youtube.videos().update(
                part="snippet",
                body={
                    "id": video_id,
                    "snippet": {
                        "title": new_title,
                        "description": f"Updated via AEON Phase 5. Transmuting old energy into new wealth.",
                        "tags": optimized_tags,
                        "categoryId": "20"
                    }
                }
            ).execute()
            print(f"[GROUNDED] {video_id}: Frequency Aligned.")
        except Exception as e:
            print(f"[RESISTANCE] {video_id}: {e}")

if __name__ == "__main__":
    # Execute for "Sea of Thieves" or any game in your 407-file Sanctuary
    mass_realign_wealth("Sea of Thieves")