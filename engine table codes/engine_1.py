import pandas as pd
import re

# Path to the CSV file
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(path)

# Function to extract structured information from the body column
def extract_details(text):
    if isinstance(text, str):
        # Regex to capture Rolls Royce and all details till 'R'
        match = re.search(r'(Rolls Royce)(.*?)(\d.*?\bR\b)', text, re.DOTALL)
        if match:
            manufacturer = match.group(1).strip()  # Rolls Royce
            details = f"{match.group(2).strip()} {match.group(3).strip()}"  # All details up to R
            return {
                'manufacturer': manufacturer,
                'details': details
            }
    return None

extracted_info = df['body'].apply(extract_details).apply(pd.Series)
# Merge extracted information back into the DataFrame
df = pd.concat([df, extracted_info], axis=1)
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\engine_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
