import pandas as pd
import re

# Load the CSV file into a DataFrame
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

# Define a function to extract the serial number from the body column
def extract_serial_number(text):
    if isinstance(text, str):
        # Use regex to find "Serial # <number>" pattern
        match = re.search(r'Serial # (\d+)', text)
        if match:
            return match.group(1)  # Return the number part of the match
    return None  # Return None if no serial number is found

# Apply the function to the 'body' column and create a new column for the serial number
df['serial_number'] = df['body'].apply(extract_serial_number)

print(df[['body', 'serial_number']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Serial_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
