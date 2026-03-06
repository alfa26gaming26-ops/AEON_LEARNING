import pickle
from googleapiclient.discovery import build

def create_wealth_funnel(playlist_title, video_ids):
    print(f"--- PHASE 5: GROUNDING PLAYLIST: {playlist_title} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # 1. INSERT: Physically creating the playlist in the YouTube plane
    playlist_response = youtube.playlists().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": f"Sovereign Tides | {playlist_title}",
                "description": "Optimized Phase 5 calibration for maximum watch time."
            },
            "status": {"privacyStatus": "public"}
        }
    ).execute()
    
    playlist_id = playlist_response['id']
    print(f"SUCCESS: Playlist {playlist_id} is active.")

    # 2. POPULATE: Gripping videos and seating them in the loop
    for video_id in video_ids:
        youtube.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()
        print(f"[GROUNDED] Video {video_id} added to funnel.")

if __name__ == "__main__":
    # Your top Sea of Thieves assets for the first funnel
    sea_of_thieves_vids = ["SlHyrZ5rd-I", "07ZKjYjwkMU", "k1G2jB32POQ"]
    create_wealth_funnel("Sea of Thieves Master Class", sea_of_thieves_vids)