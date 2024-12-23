import pandas as pd
import re

giv_path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\GIV.csv'
giv_data = pd.read_csv(giv_path)

def refine_base_table_extraction(body_text):
    base_table = {
        "MFR": None,
        "Model": None,
        "Reg": None,
        "Price": None,
        "TTAF": None,
        "Paint_Year": None,
        "Interior_Year": None,
    }
    mfr_pattern = r"(?:Manufacturer|MFR|Make)[:\s]*([\w\s]+)"
    model_pattern = r"(?:Model)[:\s]*([\w\-]+)"
    reg_pattern = r"(?:Reg|Registration)[:\s]*([A-Z0-9\-]+)"
    price_pattern = r"(?:Price)[:\s]*(Call for price|Inquire|\$[\d,]+)"
    tt_pattern = r"(?:Total Time|TTAF)[:\s]*([\d,]+)"
    paint_pattern = r"(?:Paint(ed)? Year)[:\s]*(\d{4})"
    interior_pattern = r"(?:Interior Year)[:\s]*(\d{4})"

    base_table["MFR"] = re.search(mfr_pattern, body_text, re.IGNORECASE)
    base_table["Model"] = re.search(model_pattern, body_text, re.IGNORECASE)
    base_table["Reg"] = re.search(reg_pattern, body_text, re.IGNORECASE)
    base_table["Price"] = re.search(price_pattern, body_text, re.IGNORECASE)
    base_table["TTAF"] = re.search(tt_pattern, body_text, re.IGNORECASE)
    base_table["Paint_Year"] = re.search(paint_pattern, body_text, re.IGNORECASE)
    base_table["Interior_Year"] = re.search(interior_pattern, body_text, re.IGNORECASE)

    for key, match in base_table.items():
        if match:
            value = match.group(1).strip()
            if key in ["TTAF", "Price"]:
                value = value.replace(",", "").replace("$", "").strip() 
            if key == "Reg": 
                if "ister" in value.lower():
                    value = "register" if "register" in value.lower() else "unregister"
            base_table[key] = value

    return base_table

refined_base_table_data = giv_data['body'].apply(refine_base_table_extraction)

refined_base_table_df = pd.DataFrame(refined_base_table_data.tolist())

refined_base_table_df.to_csv('Base_Table.csv', index=False)
refined_base_table_df.head()


