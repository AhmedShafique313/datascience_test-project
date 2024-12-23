import pandas as pd

path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\cleaned_aircraft_data.csv'
df = pd.read_csv(path)
selected_column = df['Model']
manufacturer_year_dict = ['1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']

def find_manufacturer(text):
    if isinstance(text, str):
        for manufacturer in manufacturer_year_dict:
            if manufacturer in text:
                return manufacturer
    return None

df['year of manufacture'] = df['Model'].apply(find_manufacturer)
print(df[['Model', 'year of manufacture']])
df.to_csv(path, index=False)
print("The original CSV file has been updated.")
