import pickle
import os
from googleapiclient.discovery import build

def get_youtube_service():
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    return build('youtube', 'v3', credentials=creds)

def fetch_and_manage_assets():
    youtube = get_youtube_service()
    print("--- Phase 5: Sanctuary Asset Audit ---")
    
    # 1. Fetch all videos from your channel
    # We use search.list with forMine=True to see your own content
    request = youtube.search().list(
        part="snippet",
        forMine=True,
        type="video",
        maxResults=50
    )
    response = request.execute()
    
    videos = response.get('items', [])
    if not videos:
        print("No digital assets found in the current frequency.")
        return

    print(f"Found {len(videos)} assets. Analyzing engagement...")
    
    for item in videos:
        v_id = item['id']['videoId']
        title = item['snippet']['title']
        
        # 2. Check statistics for engagement
        stats_req = youtube.videos().list(part="statistics", id=v_id)
        stats_res = stats_req.execute()
        views = int(stats_res['items'][0]['statistics'].get('viewCount', 0))
        
        print(f"ID: {v_id} | Views: {views} | Title: {title}")
        
        # 3. Strategy: Deletion Logic for Zero Engagement
        if views == 0:
            confirm = input(f"Transmute (Delete) {v_id} for reposting? (y/n): ")
            if confirm.lower() == 'y':
                youtube.videos().delete(id=v_id).execute()
                print(f"SUCCESS: {v_id} reclaimed for Sovereign Tides optimization.")

if __name__ == "__main__":
    fetch_and_manage_assets()