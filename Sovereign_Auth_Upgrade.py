import os
import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# PHASE 5: ELITE AUTHENTICATION UPGRADE
# Adding the 'youtube' scope for full Write/Edit authority
SCOPES = ['https://www.googleapis.com/auth/youtube']

def upgrade_to_elite_auth():
    print("--- PHASE 5: UPGRADING TO ELITE AUTHENTICATION ---")
    creds = None
    
    # Looking for the physical handshake file
    if os.path.exists('token.json'):
        os.remove('token.json') # Removing the low-authority token
        print("REMOVING DRAIN: Old token purged.")

    flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
    creds = flow.run_local_server(port=0)

    # Grounding the new Elite Token in the Sanctuary
    with open('token.json', 'wb') as token:
        pickle.dump(creds, token)
    print("SUCCESS: Elite token.json is grounded. Authority Confirmed.")

if __name__ == "__main__":
    upgrade_to_elite_auth()