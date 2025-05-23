import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("forecast_data.csv")

# Check if 'icon' and 'code' columns exist before dropping them
columns_to_drop = ['icon', 'code']
existing_columns = set(df.columns)
columns_to_drop = [col for col in columns_to_drop if col in existing_columns]

# Drop the existing columns
df.drop(columns=columns_to_drop, inplace=True)

# Extract the 'text' value from the 'condition' column
df['condition'] = df['condition'].apply(lambda x: eval(x)['text'])

# Save the modified DataFrame back to a new CSV file
df.to_csv("modified_forecast_data.csv", index=False)
