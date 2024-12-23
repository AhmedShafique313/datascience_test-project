import pandas as pd

# Load the CSV file
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)

# List of valid manufacturers and their models
manufacturer_models = {
    'Gulfstream': ['G-IVSP', 'G-V', 'G550', 'G650'],
    'Cessna': ['Citation X', 'Citation CJ4', 'Citation Latitude'],
    'Beechcraft': ['King Air 350', 'King Air 250', 'Baron 58'],
    'Piper': ['M350', 'M600', 'Aerostar'],
    'Boeing': ['737', '747', '787', '777'],
    'Dassault Aviation': ['Falcon 7X', 'Falcon 900LX', 'Falcon 2000LXS'],
    'Embraer': ['Phenom 300', 'Legacy 500', 'Lineage 1000E'],
    'Airbus': ['A320', 'A330', 'A350', 'A380']
}

# Function to find the model from the text
def find_model(text):
    if isinstance(text, str):
        for manufacturer, models in manufacturer_models.items():
            for model in models:
                if model in text:
                    return model
    return None

# Apply the function to extract the model
df['model'] = df['body'].apply(find_model)

# Print the updated DataFrame with model names
print(df[['body', 'model']])

# Save the updated DataFrame to a new CSV file
output_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\listing\extracted_datas\Models_only_GIV.csv'
df.to_csv(output_path, index=False)

print(f"Updated CSV file has been saved at {output_path}.")
