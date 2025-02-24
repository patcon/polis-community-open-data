import pandas as pd

# URL of the public Google Sheet CSV export
# See: https://docs.google.com/spreadsheets/d/1PnuFfLN8TNNA_7z83VAmczrmQYTzGEGA5hcQ9z5aP_8/edit?gid=0#gid=0
CSV_URL = "https://docs.google.com/spreadsheets/d/1PnuFfLN8TNNA_7z83VAmczrmQYTzGEGA5hcQ9z5aP_8/export?format=csv&gid=0"

# Load the CSV data
df = pd.read_csv(CSV_URL, parse_dates=["Date Created"])

# Sort by "Date Created" (oldest first)
df = df.sort_values(by="Date Created", ascending=True)

# Strip commas out of numeric fields, and set to nullable int type.
df['# Voters'] = df['# Voters'].str.replace(',', '').astype('Int64')

# Filter for only rows where "Closed?" is "✅ yes"
closed_df = df[df["Closed?"] == "✅ yes"]

# Save the trimmed CSV with only closed conversations
output_file = "conversations.csv"
closed_df.to_csv(output_file, index=False)

# Print the results
print(f"Filtered CSV saved as {output_file}")

