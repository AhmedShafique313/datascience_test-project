import pandas as pd

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
df = pd.read_csv(path)
selected_column = df['body']
manufacturer_year_dict = ['1985', '1987', '1990', '1993', '1997', '2000', '2003', '2005', '2008', '2013']

def find_manufacturer(text):
    if isinstance(text, str):
        for manufacturer in manufacturer_year_dict:
            if manufacturer in text:
                return manufacturer
    return None

df['manufacture'] = df['body'].apply(find_manufacturer)
print(df[['body', 'manufacture']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\listing\extracted_datas\Manufacture_only_GIV.csv', index=False)
print("Updated CSV file has been saved.")