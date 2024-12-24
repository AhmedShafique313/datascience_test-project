import pandas as pd

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\cleaned_aircraft_data.csv'
df = pd.read_csv(path)
selected_column = df['Model']

valid_manufacturers = ['Gulfstream', 'Cessna', 'Beechcraft', 'Piper', 'Boeing', 'Dassault Aviation', 'Embraer', 'Airbus']

def find_manufacturer(text):
    if isinstance(text, str):
        for manufacturer in valid_manufacturers:
            if manufacturer in text:
                return manufacturer
    return None

df['manufacture'] = df['Model'].apply(find_manufacturer)
print(df[['Model', 'manufacture']])
df.to_csv(path, index=False)
print("The original CSV file has been updated.")
