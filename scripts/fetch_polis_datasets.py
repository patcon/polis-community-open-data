import pandas as pd
from urllib.parse import urlparse
from reddwarf.data_loader import Loader

CSV_FILE = "conversations.csv"

# Load the CSV data
df = pd.read_csv(CSV_FILE)

# Get an array of all the conversation URLs
conversation_urls = df["Conversation URL"].dropna().tolist()
convo_ids = [urlparse(url).path.split('/')[-1] for url in conversation_urls]

print("Closed conversation IDs:")
for cid in convo_ids:
    Loader(conversation_id=cid, output_dir=f"data/{cid}")
    raise
