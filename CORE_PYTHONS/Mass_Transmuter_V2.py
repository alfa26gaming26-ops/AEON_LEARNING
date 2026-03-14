import pickle
from googleapiclient.discovery import build

def mass_realign_wealth_v2(game_topic):
    print(f"--- PHASE 5: MASS TRANSMUTING ASSETS ({game_topic}) ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # Scanning for the first 50 Amazing Units
    request = youtube.search().list(
        part="snippet",
        forMine=True,
        maxResults=50,
        type="video",
        q=game_topic
    )
    response = request.execute()

    optimized_tags = [game_topic, "Sovereign Tides", "Phase 5", "2026", "Spirit Tech"]
    
    for item in response['items']:
        video_id = item['id']['videoId']
        # SAFETY GRIP: Ensuring the title is never empty
        current_title = item['snippet'].get('title', 'Sovereign Archive')
        new_title = f"Sovereign Tides: {current_title}"[:100] # YouTube 100-char limit
        
        try:
            youtube.videos().update(
                part="snippet",
                body={
                    "id": video_id,
                    "snippet": {
                        "title": new_title,
                        "description": f"Phase 5 Calibration: Transmuting {game_topic} into wealth.",
                        "tags": optimized_tags,
                        "categoryId": "20"
                    }
                }
            ).execute()
            print(f"[GROUNDED] {video_id}: Frequency Aligned.")
        except Exception as e:
            print(f"[RESISTANCE] {video_id}: Metadata Drain - {e}")

if __name__ == "__main__":
    mass_realign_wealth_v2("Sea of Thieves")