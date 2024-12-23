import pandas as pd

giv_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'

giv_data = pd.read_csv(giv_path, encoding='utf-8')
print(giv_data.head())