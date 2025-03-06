import pandas as pd
from urllib.parse import urlparse
from reddwarf.data_loader import Loader

CSV_FILE = "conversations.csv"

# votes.json files are large.
# > 50MB: Warning to use git-lfs.
# > 100MB: Failure, can't push.
SKIP_CONVO_IDS = [
    "9xnndurbfm", #  56 MB (warning)
    "5tzfrp5eaa", #  64 MB (warning)
    "4uf4hkunf3", # 422 MB (failure)
]

# Load the CSV data
df = pd.read_csv(CSV_FILE)

# Sort so that smaller conversations come first.
df = df.sort_values(by="# Voters")

def get_id_from_url(convo_url: str) -> str:
    return urlparse(convo_url).path.split('/')[-1]

for _, row in df.iterrows():
    convo_id = get_id_from_url(row["Conversation URL"])
    if convo_id in SKIP_CONVO_IDS:
        print(f"Skipping conversation {convo_id}... ({row['# Voters']} participants)")
        continue
    print(f"Processing conversation {convo_id}... ({row['# Voters']} participants)")
    Loader(conversation_id=convo_id, output_dir=f"data/{convo_id}")
