import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
file_path = 'C:/Users/Subhradip Debray/Downloads/train/forecast_data.csv'  # Replace with your actual file path
weather_data = pd.read_csv(file_path)

# Identify non-numeric columns
non_numeric_cols = weather_data.select_dtypes(exclude=[np.number]).columns
print("Non-numeric columns:", non_numeric_cols)

# Try converting non-numeric columns to numeric if possible
for col in non_numeric_cols:
    weather_data[col] = pd.to_numeric(weather_data[col], errors='coerce')

# After conversion, check if there are any remaining non-numeric columns
non_numeric_cols_after_conversion = weather_data.select_dtypes(exclude=[np.number]).columns
print("Non-numeric columns after conversion:", non_numeric_cols_after_conversion)

# Select only numeric columns for analysis
numeric_cols = weather_data.select_dtypes(include=[np.number])

# Include the 'will_it_rain' column if it exists in the dataset
if 'will_it_rain' in weather_data.columns:
    # Drop 'will_it_rain' from numeric columns
    numeric_cols = numeric_cols.drop(columns=['will_it_rain'])

# Group by 'will_it_rain' and compute the mean for numeric columns
mean_values = numeric_cols.groupby(weather_data['will_it_rain']).mean()

# Set option to display wider output
pd.set_option('display.width', None)

# Print the mean values
print(mean_values)
