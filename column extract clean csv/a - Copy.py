import pandas as pd
import json

# Load the CSV file into a DataFrame with low_memory=False
df = pd.read_csv("forecast_data.csv", low_memory=False)

# Check if 'icon' and 'code' columns exist before dropping them
columns_to_drop = ['icon', 'code']
existing_columns = set(df.columns)
columns_to_drop = [col for col in columns_to_drop if col in existing_columns]

# Drop the existing columns
df.drop(columns=columns_to_drop, inplace=True)

# Inspect a few values from the 'condition' column to understand the formatting issue
print("Sample 'condition' values before processing:")
print(df['condition'].head(10))

# Function to fix JSON formatting issues
def fix_json_format(condition):
    if not isinstance(condition, str):
        return "error: not a string"
    try:
        # Attempt to load the JSON string to see if it's already correct
        return json.loads(condition)['text']
    except json.JSONDecodeError:
        # If JSONDecodeError, try to fix the string formatting
        try:
            condition_fixed = condition.replace("'", "\"")  # Replace single quotes with double quotes
            return json.loads(condition_fixed)['text']
        except (json.JSONDecodeError, KeyError) as e:
            return f"error: {str(e)}"

# Apply the function to the 'condition' column
df['condition'] = df['condition'].apply(fix_json_format)

# Save the modified DataFrame back to a new CSV file
df.to_csv("modified_forecast_data.csv", index=False)

# Detecting unusual or differing values
unusual_values = df[df['condition'].str.startswith('error')]

print("Extracted condition text:")
print(df['condition'])
print("\nUnusual values detected:")
print(unusual_values)
