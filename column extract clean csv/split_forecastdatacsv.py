import pandas as pd
import os

# Load the big CSV
df = pd.read_csv("column extract clean csv/forecast_data.csv")

# Split into 2 parts (adjust if needed)
n = len(df)
half = n // 2

# Create directory for split files
os.makedirs("column extract clean csv/split", exist_ok=True)

# Save split parts
df[:half].to_csv("column extract clean csv/split/forecast_part1.csv", index=False)
df[half:].to_csv("column extract clean csv/split/forecast_part2.csv", index=False)

print("✅ File split complete!")
