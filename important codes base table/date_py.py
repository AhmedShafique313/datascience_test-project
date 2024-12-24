import pandas as pd
import re

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

def extract_advertisement_date(text):
    if isinstance(text, str):
        match = re.search(r'\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{1,2}\b', text, re.IGNORECASE)
        if match:
            return match.group(0)
    return None

df['advertisement_date'] = df['body'].apply(extract_advertisement_date)
print(df[['body', 'advertisement_date']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Date_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
