import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

# Load the GIV.csv file
data = pd.read_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv')

# Function to extract relevant information from the body text
def extract_info(body_text):
    extracted_info = {
        'Model': None,
        'Registration': None,
        'TTAF': None,
        'Price': None,
        'Engine Hours': None,
        'Maintenance Plan': None
    }
    
    # Regex patterns to extract information
    model_pattern = r'(\d{4} Gulfstream [A-Z0-9\-]+)'
    reg_pattern = r'Reg # ([A-Z0-9]+)'
    ttaf_pattern = r'TTAF: ([\d,]+) Hrs\.'
    price_pattern = r'Price: (.+?)(?=\n|$)'
    engine_hours_pattern = r'Engines.*?(\d+ Hrs\.)'
    maintenance_pattern = r'Maintenance Plan: (Yes|No)'

    # Extracting information using regex
    model_match = re.search(model_pattern, body_text)
    reg_match = re.search(reg_pattern, body_text)
    ttaf_match = re.search(ttaf_pattern, body_text)
    price_match = re.search(price_pattern, body_text)
    engine_hours_match = re.search(engine_hours_pattern, body_text, re.DOTALL)
    maintenance_match = re.search(maintenance_pattern, body_text)

    if model_match:
        extracted_info['Model'] = model_match.group(1)
    if reg_match:
        extracted_info['Registration'] = reg_match.group(1)
    if ttaf_match:
        extracted_info['TTAF'] = ttaf_match.group(1)
    if price_match:
        extracted_info['Price'] = price_match.group(1).strip()
    if engine_hours_match:
        extracted_info['Engine Hours'] = engine_hours_match.group(1)
    if maintenance_match:
        extracted_info['Maintenance Plan'] = maintenance_match.group(1)

    return extracted_info

# Apply the extraction function to the body column
data['Extracted Info'] = data['body'].apply(extract_info)

# Convert the extracted information into a DataFrame
extracted_df = pd.json_normalize(data['Extracted Info'])

# Data Cleaning
# Convert TTAF to integer, replacing None with NaN first
extracted_df['TTAF'] = extracted_df['TTAF'].str.replace(',', '').replace('None', None)
extracted_df['TTAF'] = pd.to_numeric(extracted_df['TTAF'], errors='coerce')

# Check for NaN values in TTAF and decide how to handle them
print("NaN values in TTAF:", extracted_df['TTAF'].isna().sum())

# Clean Price: Remove dollar sign and commas, convert to float
extracted_df['Price'] = extracted_df['Price'].replace({'\$': '', ',': ''}, regex=True).replace('Inquire', None)
extracted_df['Price'] = pd.to_numeric(extracted_df['Price'], errors='coerce')

# Check for missing values
print(extracted_df.isnull().sum())

# Descriptive Statistics
print(extracted_df.describe())

# Plotting TTAF distribution
plt.figure(figsize=(10, 6))
sns.histplot(extracted_df['TTAF'], bins=20, kde=True)
plt.title('Distribution of Total Time Airframe (TTAF)')
plt.xlabel('TTAF (Hours)')
plt.ylabel('Frequency')
plt.show()

# Filter aircraft with TTAF greater than 5000 hours
high_ttaf = extracted_df[extracted_df['TTAF'] > 5000]
print(high_ttaf)

# Save cleaned data to a new CSV file
extracted_df.to_csv('cleaned_aircraft_data.csv', index=False)

# Display the first few rows of the cleaned data
print(extracted_df.head())