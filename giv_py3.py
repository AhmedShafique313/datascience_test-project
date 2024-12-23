import re
import pandas as pd
from giv_py2 import refine_base_table_extraction

giv_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
giv_data = pd.read_csv(giv_path)
def preprocess_text(text):
    text = re.sub(r'\n', ' ', text) 
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

giv_data['cleaned_body'] = giv_data['body'].apply(preprocess_text)
preprocessed_base_table_data = giv_data['cleaned_body'].apply(refine_base_table_extraction)
preprocessed_base_table_df = pd.DataFrame(preprocessed_base_table_data.tolist())
preprocessed_base_table_df.to_csv('Base_Table_Preprocessed.csv', index=False)
print(preprocessed_base_table_df.head())