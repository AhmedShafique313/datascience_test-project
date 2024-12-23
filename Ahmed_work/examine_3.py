import pandas as pd

giv_short_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIVshort.csv'
target_data_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\TargetData-Red.xlsx'
base_table_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\Base_Table.csv'

giv_short = pd.read_csv(giv_short_path)
target_data = pd.read_excel(target_data_path, sheet_name=None)
base_table = pd.read_csv(base_table_path)

giv_short_head = giv_short.head()
base_table_head = base_table.head()
target_data_keys = list(target_data.keys())
# print('GIV Short File')
# print(giv_short_head)
# print('Base File')
# print(base_table_head)
# print('Target file')
# print(target_data_keys)

body_sample = giv_short['body'].sample(3, random_state=42) 

print(body_sample.tolist())
