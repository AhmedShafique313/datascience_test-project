import pandas as pd
import re

# Load the data
df = pd.read_csv(r"C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv")

# Function to extract data from the body column
def extract_details(text):
    details = {
        "manufacturer_model": None,
        "registration_number": None,
        "engine_hours": None,
        "maintenance_plan": None,
    }
    
    # Manufacturer and Model
    model_match = re.search(r"(\d{4}\s[\w\s\-]+G-IV\S*)", text)
    if model_match:
        details["manufacturer_model"] = model_match.group(1)
    
    # Registration Number
    reg_match = re.search(r"Reg\s#\s([\w\d\-]+)", text)
    if reg_match:
        details["registration_number"] = reg_match.group(1)
    
    # Engine Hours
    hours_match = re.search(r"TTAF:\s([\d,]+)\sHrs\.", text)
    if hours_match:
        details["engine_hours"] = hours_match.group(1).replace(",", "")
    
    # Maintenance Plan
    if "Maintenance Plan" in text or "Aircraft Maintenance Tracking Vehicle" in text:
        details["maintenance_plan"] = "Yes"
    else:
        details["maintenance_plan"] = "No"
    
    return details

# Apply the extraction function to the body column
extracted_data = df["body"].apply(extract_details)
extracted_df = pd.DataFrame(extracted_data.tolist())

# Combine the extracted data with the original dataframe
df = pd.concat([df, extracted_df], axis=1)

# Save the results to a new CSV file
df.to_csv(r"C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Ahmed_work/Extracted_Aircraft_Data2.csv", index=False)

print("Extraction complete. Data saved to 'Extracted_Aircraft_Data2.csv'")
