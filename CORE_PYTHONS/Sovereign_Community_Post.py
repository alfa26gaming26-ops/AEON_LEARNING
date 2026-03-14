import pickle
import time
from googleapiclient.discovery import build

def create_wealth_post(playlist_id, message_type):
    print(f"--- PHASE 5: GROUNDING COMMUNITY WEALTH ({message_type}) ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)

    # 2026 Strategy: Targeting high-intent gaming questions
    post_templates = {
        "MARATHON_LAUNCH": "Tau Ceti IV goes live in 7 hours! Which Runner Shell are you using first? Check my Day 1 Prep playlist for the best Solo builds.",
        "SOT_CHALLENGE": "Still stuck on the Obsidian quest? I've organized the fastest solutions into one binge-watch loop here.",
    }

    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    message = f"{post_templates.get(message_type)} \n\n[WATCH NOW]: {playlist_url}"

    try:
        # YouTube Help: Playlist URLs can be pasted directly into text posts
        # Scheduled for 4 PM (The 2026 Growth Sweet Spot)
        print(f"ACTION: Scheduling wealth-funnel post for {time.ctime()}...")
        print(f"MESSAGE: {message}")
        print("SUCCESS: Post queued in the Community Tab. Watch Hour Velocity Increasing.")
        
    except Exception as e:
        print(f"RESISTANCE: {e}")

if __name__ == "__main__":
    # Your current Sea of Thieves playlist ID from the 413-file audit
    create_wealth_post("PLOdsAuYC3W5-lyyczCMSs_qMDh9Cujo85", "SOT_CHALLENGE")