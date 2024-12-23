import pandas as pd
import re

# Load the GIVshort.csv file
giv_short_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv'
giv_short = pd.read_csv(giv_short_path)

# Define a function to extract details from the 'body' column
def extract_details(text):
    details = {
        'advert_date': None,
        'manufacturer': None,
        'model': None,
        'registration_number': None,
        'engine_hours': None,
        'maintenance_plan': None,
    }

    if pd.isna(text):
        return details

    # Extract advertisement date (e.g., "Posted on: Jan 1, 2023")
    date_match = re.search(r'Posted on[:\-]?\s?(\w+\s\d{1,2},\s\d{4})', text)
    if date_match:
        details['advert_date'] = date_match.group(1)

    # Extract manufacturer and model (e.g., "GULFSTREAM GIV")
    manufacturer_model_match = re.search(r'(GULFSTREAM|CESSNA|BEECHCRAFT|PIPER|BOEING)\s([A-Za-z0-9\-]+)', text)
    if manufacturer_model_match:
        details['manufacturer'] = manufacturer_model_match.group(1)
        details['model'] = manufacturer_model_match.group(2)

    # Extract registration number (e.g., "Registration No: N970SJ")
    reg_match = re.search(r'Registration\sNo[:\-]?\s?(\w+)', text)
    if reg_match:
        details['registration_number'] = reg_match.group(1)

    # Extract engine hours (e.g., "4500 hours")
    hours_match = re.search(r'(\d{1,5})\s?hours', text)
    if hours_match:
        details['engine_hours'] = hours_match.group(1)

    # Extract maintenance plan (e.g., "Maintenance Plan: GE")
    maintenance_match = re.search(r'Maintenance Plan[:\-]?\s?(\w+)', text)
    if maintenance_match:
        details['maintenance_plan'] = maintenance_match.group(1)

    return details

# Apply the function to the 'body' column
extracted_data = giv_short['body'].apply(extract_details)

# Convert the extracted data into a DataFrame
extracted_df = pd.DataFrame(extracted_data.tolist())

# Combine extracted data with original DataFrame for reference
result_df = pd.concat([giv_short, extracted_df], axis=1)

# Save the result to a new CSV file
output_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Ahmed_work/Extracted_Aircraft_Data.csv'
result_df.to_csv(output_path, index=False)

print(f"Extraction completed. Data saved to {output_path}.")
