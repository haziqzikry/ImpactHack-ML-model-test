import json
import pandas as pd

# Load JSON data
with open('inventory_data.json') as json_file:
    data = json.load(json_file)

# Convert JSON data to pandas DataFrame
df = pd.DataFrame(data)

# Define the threshold for high demand
demand_threshold = 50  # Adjust the threshold based on your domain knowledge

# Create the target column "Product Demand"
df['Product Demand'] = df['Number of products sold'].apply(lambda x: 1 if x > demand_threshold else 0)

# Save the updated DataFrame to a new JSON file
updated_data = df.to_dict(orient='records')

with open('updated_inventory_data.json', 'w') as json_file:
    json.dump(updated_data, json_file, indent=4)
