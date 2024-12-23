import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv')

# Function to extract relevant information from the body text
def extract_info(body_text):
    extracted_info = {
        'Model': None,
        'Registration': None,
        'TTAF': None,
        'Price': None,
        'Engine Hours': None,
    }
    
    model_pattern = r'(\d{4} Gulfstream [A-Z0-9\-]+)'
    reg_pattern = r'Reg # ([A-Z0-9]+)'
    ttaf_pattern = r'TTAF: ([\d,]+) Hrs\.'
    price_pattern = r'Price: (.+?)(?=\n|$)'
    engine_hours_pattern = r'Engines.*?(\d+ Hrs\.)'

    model_match = re.search(model_pattern, body_text)
    reg_match = re.search(reg_pattern, body_text)
    ttaf_match = re.search(ttaf_pattern, body_text)
    price_match = re.search(price_pattern, body_text)
    engine_hours_match = re.search(engine_hours_pattern, body_text, re.DOTALL)

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

    return extracted_info

data['Extracted Info'] = data['body'].apply(extract_info)

extracted_df = pd.json_normalize(data['Extracted Info'])

extracted_df['TTAF'] = extracted_df['TTAF'].str.replace(',', '').replace('None', None)
extracted_df['TTAF'] = pd.to_numeric(extracted_df['TTAF'], errors='coerce')

print("NaN values in TTAF:", extracted_df['TTAF'].isna().sum())

extracted_df['Price'] = extracted_df['Price'].replace({'\$': '', ',': ''}, regex=True).replace('Inquire', None)
extracted_df['Price'] = pd.to_numeric(extracted_df['Price'], errors='coerce')

print(extracted_df.isnull().sum())
print(extracted_df.describe())
plt.figure(figsize=(10, 6))
sns.histplot(extracted_df['TTAF'], bins=20, kde=True)
plt.title('Distribution of Total Time Airframe (TTAF)')
plt.xlabel('TTAF (Hours)')
plt.ylabel('Frequency')
plt.show()

high_ttaf = extracted_df[extracted_df['TTAF'] > 5000]
print(high_ttaf)

extracted_df.to_csv('cleaned_aircraft_data.csv', index=False)
print(extracted_df.head())