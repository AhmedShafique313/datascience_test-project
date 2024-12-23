import pandas as pd
import re

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

def extract_refurb_date(text):
    if isinstance(text, str):
        match = re.search(r'(?:Refurbished|New paint -)\s(\d{4})', text, re.IGNORECASE)
        if match:
            return match.group(1)
    return None 

df['refurb_date'] = df['body'].apply(extract_refurb_date)

print(df[['body', 'refurb_date']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Paint_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
