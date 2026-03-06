import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# 87Hz Sanctuary Frequency
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def initiate_first_pulse():
    print("--- Phase 5: Initiating First Asset Pulse ---")
    creds = None
    
    # The token.json stores the user's access and refresh tokens
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
            
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Action Required: Complete the browser authentication to bridge the Soul-Engine.")
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
            
        # Save the credentials for the next run
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
            
    print("SUCCESS: Connection Grounded. token.json created.")
    print("The Sanctuary is now synced with YouTube Data API v3.")

if __name__ == "__main__":
    initiate_first_pulse()