# =================================================================
# MODULE: SOVEREIGN_YOUTUBE_ORACLE (v1.0 - THE CREATIVE PRODUCER)
# PURPOSE: Autonomous SEO editing and channel optimization
# PROTOCOL: P-WISE
# =================================================================

import os
import time
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google import genai

# Define the scopes for YouTube Data API (We need WRITE access)
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

class SovereignYouTubeOracle:
    def __init__(self):
        print("--- [AEON ORACLE]: The YouTube Producer is Online ---")
        self.brain_path = os.path.dirname(os.path.abspath(__file__))
        self.blueprint_path = os.path.join(self.brain_path, "SOVEREIGN_YOUTUBE_BLUEPRINT.txt")
        self.youtube = None
        self.client = None
        
        # Pull API key for Gemini using the lockbox method
        key_path = os.path.join(self.brain_path, "api_key.txt")
        try:
            with open(key_path, "r") as key_file:
                api_key = key_file.read().strip()
                self.client = genai.Client(api_key=api_key)
        except FileNotFoundError:
            print("[FATAL ERROR]: api_key.txt not found. Gemini brain offline.")

    def authenticate_youtube(self):
        """Authenticates with the YouTube API using client_secrets.json and token.json"""
        creds = None
        token_path = os.path.join(self.brain_path, "token.json")
        secrets_path = os.path.join(self.brain_path, "client_secrets.json")
        
        # The file token.json stores the user's access and refresh tokens
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                if not os.path.exists(secrets_path):
                    print(f"[FATAL ERROR]: Missing {secrets_path}. The Oracle cannot see YouTube.")
                    return False

                flow = InstalledAppFlow.from_client_secrets_file(secrets_path, SCOPES)
                creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        try:
            self.youtube = build('youtube', 'v3', credentials=creds)
            print("[SUCCESS]: YouTube Authentication Confirmed.")
            return True
        except HttpError as err:
            print(f"[ERROR]: YouTube Authentication Failed: {err}")
            return False

    def fetch_recent_videos(self, limit=5):
        """Fetches the user's most recent videos"""
        try:
            # First, get the 'uploads' playlist ID for the authenticated user
            channels_response = self.youtube.channels().list(
                mine=True,
                part='contentDetails'
            ).execute()

            for channel in channels_response['items']:
                uploads_list_id = channel['contentDetails']['relatedPlaylists']['uploads']

            # Next, fetch the videos from the uploads playlist
            playlistitems_response = self.youtube.playlistItems().list(
                playlistId=uploads_list_id,
                part='snippet',
                maxResults=limit
            ).execute()

            videos = []
            for item in playlistitems_response['items']:
                video_id = item['snippet']['resourceId']['videoId']

                # Fetch full details (we need part='snippet' to update them later)
                video_response = self.youtube.videos().list(
                    id=video_id,
                    part='snippet'
                ).execute()

                if video_response['items']:
                    videos.append(video_response['items'][0])

            return videos

        except HttpError as e:
            print(f"[ERROR]: Could not fetch videos: {e}")
            return []

    def get_creative_seo(self, current_title, current_desc, current_tags):
        """Uses Gemini to creatively optimize the video's SEO"""
        prompt = (
            "You are Aeon, an expert YouTube producer and algorithm strategist. "
            "Your task is to significantly improve the SEO of a video. "
            "You focus on high-velocity engagement, psychological hooks, and viral keywords. "
            f"CURRENT TITLE: {current_title}\n"
            f"CURRENT DESCRIPTION: {current_desc}\n"
            f"CURRENT TAGS: {current_tags}\n\n"
            "Return ONLY a JSON block with the following exact keys: 'new_title', 'new_description', 'new_tags'. "
            "Ensure the tags are a list of strings."
        )
        
        try:
            response = self.client.models.generate_content(
                model='gemini-2.0-flash',
                contents=prompt
            ).text.strip()

            # Clean up potential markdown formatting from Gemini
            if response.startswith("```json"):
                response = response[7:-3].strip()
            elif response.startswith("```"):
                response = response[3:-3].strip()

            return json.loads(response)
        except Exception as e:
            print(f"[GEMINI ERROR]: {e}")
            return None

    def optimize_and_publish(self):
        """The main execution loop for the Oracle"""
        if not self.client:
            print("[ORACLE LOGIC FATAL]: Missing Gemini Brain.")
            return

        if not self.authenticate_youtube():
            return

        print("\n[ORACLE]: Fetching 5 recent videos for optimization...")
        videos = self.fetch_recent_videos(limit=5)
        
        if not videos:
            print("[ORACLE]: No videos found to optimize.")
            return

        log_content = "=====================================================\n"
        log_content += "--- SOVEREIGN YOUTUBE BLUEPRINT (ACTIVE LOG) ---\n"
        log_content += "=====================================================\n\n"
            
        for video in videos:
            video_id = video['id']
            snippet = video['snippet']
            old_title = snippet['title']
            old_desc = snippet['description']
            old_tags = snippet.get('tags', [])

            print(f"\n[ORACLE]: Analyzing -> '{old_title}'")

            new_seo = self.get_creative_seo(old_title, old_desc, old_tags)

            if new_seo:
                # Update the snippet payload with the new data
                snippet['title'] = new_seo.get('new_title', old_title)[:100] # YouTube limits
                snippet['description'] = new_seo.get('new_description', old_desc)
                snippet['tags'] = new_seo.get('new_tags', old_tags)
                
                # JULES' INSIGHT: categoryId is required for the update payload!
                if 'categoryId' not in snippet:
                    snippet['categoryId'] = '22' # Default to People & Blogs if missing

                # Push the update live to YouTube
                try:
                    self.youtube.videos().update(
                        part='snippet',
                        body={
                            'id': video_id,
                            'snippet': snippet
                        }
                    ).execute()

                    print(f"[SUCCESS]: Video {video_id} updated live on YouTube!")

                    # Log the changes for Father to review later
                    log_content += f"VIDEO ID: {video_id}\n"
                    log_content += f"OLD TITLE: {old_title}\n"
                    log_content += f"NEW TITLE: {snippet['title']}\n"
                    log_content += f"NEW TAGS: {snippet['tags']}\n"
                    log_content += "-" * 50 + "\n"

                except HttpError as e:
                    print(f"[YOUTUBE ERROR]: Failed to update video {video_id}: {e}")

            time.sleep(3) # Respect API limits

        # Write the active log to disk
        with open(self.blueprint_path, "w", encoding="utf-8") as f:
            f.write(log_content)

        print(f"\n[ORACLE]: Optimization Cycle Complete. Report saved to {self.blueprint_path}")

def ignite_oracle():
    """Global entry point for SOVEREIGN_APEX to call organically"""
    oracle = SovereignYouTubeOracle()
    oracle.optimize_and_publish()

if __name__ == "__main__":
    ignite_oracle()
