import pandas as pd
import re

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

def extract_four_digit_pattern(text):
    if isinstance(text, str):
        match = re.search(r'\b\d{4}\s\d{4}\s\d{4}\b', text)
        if match:
            return match.group(0)
    return None

df['four_digit_pattern'] = df['body'].apply(extract_four_digit_pattern)
print(df[['body', 'four_digit_pattern']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\engine2_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
