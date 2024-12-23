import pandas as pd
target_data_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\TargetData-Red.xlsx'
target_data = pd.read_excel(target_data_path, sheet_name=None)
target_data_sheet = target_data['Sheet1']

target_data_sheet_head = target_data_sheet.head()
print(target_data_sheet_head)
