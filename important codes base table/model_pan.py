import pandas as pd

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\cleaned_aircraft_data.csv'
df = pd.read_csv(path)

manufacturer_models = {
    'Gulfstream': ['G-IVSP', 'G-IV', 'G450', 'G650', 'G550', 'G-III', 'G200', 'IVSP', 'IV', 'III'],
    'Cessna': ['Citation X', 'Citation CJ4', 'Citation Latitude'],
    'Beechcraft': ['King Air 350', 'King Air 250', 'Baron 58'],
    'Piper': ['M350', 'M600', 'Aerostar'],
    'Boeing': ['737', '747', '787', '777'],
    'Dassault Aviation': ['Falcon 7X', 'Falcon 900LX', 'Falcon 2000LXS'],
    'Embraer': ['Phenom 300', 'Legacy 500', 'Lineage 1000E'],
    'Airbus': ['A320', 'A330', 'A350', 'A380']
}

def find_model(text):
    if isinstance(text, str):
        for manufacturer, models in manufacturer_models.items():
            for model in models:
                if model in text:
                    return model
    return None

df['model'] = df['Model'].apply(find_model)
print(df[['Model', 'model']])
df.to_csv(path, index=False)
print("The original CSV file has been updated.")
