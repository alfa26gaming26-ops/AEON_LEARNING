import pickle
from googleapiclient.discovery import build

def scout_competitor_wealth(niche_queries):
    print("--- PHASE 5: SCOUTING COMPETITOR WEALTH VELOCITY ---")
    
    with open('token.json', 'rb') as token:
        creds = pickle.load(token)
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    wealth_suggestions = {}

    for query in niche_queries:
        print(f"Analyzing Frequency: {query}...")
        
        # Searching for the top 3 trending videos in your niche
        request = youtube.search().list(
            part="snippet",
            q=query,
            type="video",
            order="viewCount", # Grounding the search in high-volume views
            publishedAfter="2026-02-01T00:00:00Z", # March 2026 calibration
            maxResults=3
        )
        response = request.execute()
        
        keywords = []
        for item in response['items']:
            # Extracting the "Amazing" units from competitor titles
            title = item['snippet']['title']
            keywords.append(title)
            
        wealth_suggestions[query] = keywords

    print("\n--- DAILY WEALTH ALIGNMENT REPORT ---")
    for niche, titles in wealth_suggestions.items():
        print(f"\n[NICHE] {niche}")
        for i, t in enumerate(titles, 1):
            print(f" {i}. Target Frequency: {t}")

if __name__ == "__main__":
    # Calibrated for your current grounding and the March 5th Marathon launch
    scout_competitor_wealth(["Sea of Thieves Guide", "Marathon Bungie Gameplay"])