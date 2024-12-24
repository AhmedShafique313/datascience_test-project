import pandas as pd

# Load the CSV file into a DataFrame
path = r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\engine2_GIVshort.csv'
df = pd.read_csv(path)

# Define a function to extract the first four digits
def extract_first_four_digits(text):
    if isinstance(text, str):
        return text.split()[0]  # Split the string by spaces and take the first part
    return None  # Return None if the text is not a string

# Apply the function to the 'four_digit_pattern' column and update the column
df['tsn'] = df['four_digit_pattern'].apply(extract_first_four_digits)

# Print the DataFrame to verify the result
print(df[['four_digit_pattern', 'tsn']])
df.to_csv(r'C:\Users\Ahmed Shafique\Documents\Projects\Datascience test project\tsn_GIVshort.csv', index=False)
print("Updated CSV file has been saved.")
