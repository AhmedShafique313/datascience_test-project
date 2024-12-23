import pandas as pd
import re

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv'
df = pd.read_csv(path)
selected_column = df['body']

valid_manufacturers = ['Gulfstream', 'Cessna', 'Beechcraft', 'Piper', 'Boeing']

manufacturer_pattern = '|'.join(valid_manufacturers)  # This creates a pattern like: 'GULFSTREAM|CESSNA|BEECHCRAFT|PIPER|BOEING'

# Function to find manufacturer using regex
def find_manufacturer(text):
    # Check if the text is a valid string
    if isinstance(text, str):
        # Use regex to search for any of the valid manufacturers
        match = re.search(manufacturer_pattern, text)
        if match:
            return match.group(0)  # Return the manufacturer if found
    return None  # Return None if no match is found or text is not a string

# Apply the 'find_manufacturer' function to the 'body' column and create a new 'manufacture' column
df['manufacture'] = df['body'].apply(find_manufacturer)

# Print the resulting DataFrame (you can remove this line if not needed)
print(df[['body', 'manufacture']])

# Optionally, save the updated DataFrame to a new CSV file
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Updated_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
