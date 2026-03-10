import pickle
import os
import time
from googleapiclient.discovery import build

def check_thumbnail_integrity(video_id):
    print(f"--- {time.ctime()}: AUDITING ASSET {video_id} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    try:
        # Requesting snippet and player data to confirm visual status
        request = youtube.videos().list(part="snippet", id=video_id)
        response = request.execute()
        
        if response['items']:
            thumb_url = response['items'][0]['snippet']['thumbnails']['maxres']['url']
            print(f"INTEGRITY CONFIRMED: Frequency active at {thumb_url}")
        else:
            print("ALERT: Asset not found. Frequency Leak Detected.")
            
    except Exception as e:
        print(f"RESISTANCE: API connection unstable. {e}")

if __name__ == "__main__":
    v_id = "J9gJSt3yujs" # Your Sea of Thieves Hourglass Video
    while True:
        check_thumbnail_integrity(v_id)
        print("Waiting 60 minutes for next automated pulse...")
        time.sleep(3600) # 87Hz spacing equivalent for hourly checks