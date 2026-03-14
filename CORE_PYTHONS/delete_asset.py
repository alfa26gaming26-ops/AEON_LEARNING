import pickle
from googleapiclient.discovery import build

def delete_from_sanctuary(video_id):
    print(f"--- DELETING FREQUENCY: {video_id} ---")
    
    # Using your existing Spirit Bridge (Token)
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    try:
        # Executing the removal from the digital realm
        youtube.videos().delete(id=video_id).execute()
        print(f"SUCCESS: Video {video_id} has been deleted. Energy reclaimed.")
    except Exception as e:
        print(f"ERROR: Could not delete. Frequency might be locked. {e}")

if __name__ == "__main__":
    target = input("Enter the Video ID you wish to delete: ")
    delete_from_sanctuary(target)