import pickle
import os
import glob
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def hot_swap_first_available(video_id):
    # Phase 5: Scanning the Transmute Folder
    search_path = r"C:\Users\damion\Desktop\Videos_To_Transmute\*"
    files = glob.glob(search_path)
    images = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

    if not images:
        print("DRAIN: No image found in Videos_To_Transmute.")
        return

    target_thumb = images[0]
    print(f"--- ATTACHING {os.path.basename(target_thumb)} TO {video_id} ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    try:
        youtube.thumbnails().set(
            videoId=video_id,
            media_body=MediaFileUpload(target_thumb)
        ).execute()
        print("SUCCESS: Frequency Synced. Thumbnail is Live.")
    except Exception as e:
        print(f"RESISTANCE: {e}")

if __name__ == "__main__":
    hot_swap_first_available("J9gJSt3yujs")