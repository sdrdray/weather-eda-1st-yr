import pickle
import pandas as pd

# Step 1: Load the trained LightGBM model
model_file = './LightGBM.pkl'
with open(model_file, 'rb') as file:
    lgbm_best = pickle.load(file)

# Step 2: Prepare the new data for prediction
# Example new data for the specific day (format should match the training data)
# Replace 'value1', 'value2', etc., with actual feature values for the day you want to predict
new_data = pd.DataFrame({
    'feature1': [value1],
    'feature2': [value2],
    'feature3': [value3],
    'feature4': [value4],
    # Add all necessary features here
    # ...
})

# Step 3: Make predictions
predicted_weather = lgbm_best.predict(new_data)

# Step 4: Output the prediction
print(f"Predicted weather condition: {predicted_weather[0]}")
