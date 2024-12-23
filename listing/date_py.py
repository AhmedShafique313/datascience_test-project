import pandas as pd
import re

# Load the CSV file into a DataFrame
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

# Define a function to extract the advertisement date and time
def extract_advertisement_date(text):
    if isinstance(text, str):
        # Use regex to match the date and time pattern
        match = re.search(r'([A-Za-z]+\s\d{1,2},\s\d{2}:\d{2}\s[APM]{2}\s[\w\s]+)', text)
        if match:
            return match.group(1)  # Return the matched date and time
    return None  # Return None if no match is found

# Apply the function to the 'body' column and create a new column
df['advertisement_date'] = df['body'].apply(extract_advertisement_date)

# Print the DataFrame to verify the result
print(df[['body', 'advertisement_date']])

# Save the modified DataFrame back to the original CSV file
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Date_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
