import pandas as pd
import re

# Sample Data
data = {
    "id": [18],
    "source": ["aso"],
    "body": ["1996 Gulfstream G-IVSP 1289 N920KM for Sale: Specs, Price | ASO.com\n...\nPrice: Inquire\nTTAF: 6,513 Hrs.\nLocation: TN, US\n..."]
}

# Load Data into DataFrame
df = pd.DataFrame(data)

# Extract Relevant Information
def parse_details(body_text):
    details = {}
    details["year_model"] = re.search(r"(\d{4}) Gulfstream", body_text).group(1) if re.search(r"(\d{4}) Gulfstream", body_text) else None
    details["model"] = re.search(r"Gulfstream (\S+)", body_text).group(1) if re.search(r"Gulfstream (\S+)", body_text) else None
    details["price"] = re.search(r"Price: (.+)", body_text).group(1) if re.search(r"Price: (.+)", body_text) else "Inquire"
    details["ttaf"] = re.search(r"TTAF: ([\d,]+) Hrs\.", body_text).group(1) if re.search(r"TTAF: ([\d,]+) Hrs\.", body_text) else None
    details["location"] = re.search(r"Location: (.+?)\n", body_text).group(1) if re.search(r"Location: (.+?)\n", body_text) else None
    return details

# Apply Parsing
df_parsed = df["body"].apply(parse_details).apply(pd.Series)

# Merge with Original Data
df = pd.concat([df, df_parsed], axis=1)

# Display Processed Data
print(df)
