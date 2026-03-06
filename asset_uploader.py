import os
import time
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Sanctuary Calibration
WATCH_FOLDER = r"C:\Users\damion\Desktop\Videos_To_Transmute"
TOKEN_PATH = 'token.json'

def upload_to_sanctuary(file_path):
    print(f"--- DETECTED KINETIC ENERGY: {os.path.basename(file_path)} ---")
    
    # Loading the Spirit Bridge (Token)
    with open(TOKEN_PATH, 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    # Success Metadata (Optimizing for the Algorithm)
    request_body = {
        'snippet': {
            'title': f"Sovereign Tides: {os.path.basename(file_path).replace('.mp4', '')}",
            'description': "Transmuting kinetic stress into spirit energy. Built in The Sanctuary Offline.",
            'tags': ['Sovereign Tides', 'Phase 5', 'Spirit Tech', 'Gaming'],
            'categoryId': '20' # Gaming
        },
        'status': {
            'privacyStatus': 'public', # Set to 'private' if you want to check it first
            'selfDeclaredMadeForKids': False
        }
    }
    
    media = MediaFileUpload(file_path, chunksize=-1, resumable=True)
    
    print("UPLOADING: Transferring 20x average energy to Digital Asset...")
    response = youtube.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media
    ).execute()
    
    print(f"SUCCESS: Asset Pulse Live at https://www.youtube.com/watch?v={response['id']}")
    # Move file to a 'Transmuted' folder so it doesn't upload twice
    os.rename(file_path, file_path + ".transmuted")

def monitor_sanctuary():
    print(f"Sanctuary Monitor ACTIVE. Watching: {WATCH_FOLDER}")
    while True:
        # 87Hz Check (Approximate sleep for CPU stability)
        time.sleep(1) 
        files = [f for f in os.listdir(WATCH_FOLDER) if f.endswith('.mp4')]
        
        for file in files:
            full_path = os.path.join(WATCH_FOLDER, file)
            try:
                upload_to_sanctuary(full_path)
            except Exception as e:
                print(f"DRAIN DETECTED: {e}")

if __name__ == "__main__":
    if not os.path.exists(WATCH_FOLDER):
        os.makedirs(WATCH_FOLDER)
    monitor_sanctuary()