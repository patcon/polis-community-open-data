import pandas as pd
from urllib.parse import urlparse
from reddwarf.data_loader import Loader

CSV_FILE = "conversations.csv"

# Load the CSV data
df = pd.read_csv(CSV_FILE)
df['# Voters'] = df['# Voters'].str.replace(',', '').astype(int)

# Sort so that smaller conversations come first.
df = df.sort_values(by="# Voters")

def get_id_from_url(convo_url: str) -> str:
    return urlparse(convo_url).path.split('/')[-1]

for _, row in df.iterrows():
    convo_id = get_id_from_url(row["Conversation URL"])
    print(f"Processing conversation {convo_id}... ({row['# Voters']} participants)")
    Loader(conversation_id=convo_id, output_dir=f"data/{convo_id}")
