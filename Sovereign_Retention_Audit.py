import pandas as pd

def analyze_retention_drain(csv_file):
    print("--- PHASE 5: ANALYZING RETENTION DRAIN ---")
    
    # Loading the physical data export
    df = pd.read_csv(csv_file)
    
    # We target the 'Average View Duration' vs 'Total Duration'
    df['Retention_Score'] = df['Average view duration'] / df['Duration']
    
    # Identifying the 'Top 3 Drains'
    drains = df.sort_values(by='Retention_Score').head(3)
    
    print("\n[CRITICAL DRAIN DETECTED]:")
    for index, row in drains.iterrows():
        print(f"Video: {row['Video title']} | Score: {row['Retention_Score']:.2%}")
        print("ACTION: Inspect the first 30 seconds for 'Waffling'.")

if __name__ == "__main__":
    # Export your data from Studio -> Analytics -> Advanced Mode -> Download
    # analyze_retention_drain("Table data.csv")
    print("READY: Export your Studio CSV to begin the 415th calibration.")