import pandas as pd
import re

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

def extract_location(text):
    if isinstance(text, str):
        match = re.search(r'\b[A-Z]{2},\s[A-Z]{2}\b', text)
        if match:
            return match.group(0)
    return None

df['location'] = df['body'].apply(extract_location)
print(df[['body', 'location']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Location_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
