import pandas as pd

# Load the CSV file into a DataFrame
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\engine2_GIVshort.csv'
df = pd.read_csv(path)

# Define a function to extract the third set of four digits
def extract_third_four_digits(text):
    if isinstance(text, str):
        parts = text.split()  # Split the string by spaces
        if len(parts) > 2:    # Ensure there are at least three parts
            return parts[2]   # Return the third part
    return None  # Return None if the text is not in the expected format

# Apply the function to the 'four_digit_pattern' column and add a new column
df['tsml'] = df['four_digit_pattern'].apply(extract_third_four_digits)

# Print the DataFrame to verify the result
print(df[['four_digit_pattern', 'tsml']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\tsml_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
