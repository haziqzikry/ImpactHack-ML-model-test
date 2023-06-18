import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import json

# Load the JSON data
with open('updated_inventory_data.json') as f:
    data = json.load(f)

# Convert JSON data to a pandas DataFrame
df = pd.DataFrame(data)

# Select relevant features for demand forecasting
features = ['Product type', 'SKU', 'Price', 'Availability', 'Number of products sold', 'Revenue generated', 'Customer demographics', 'Stock levels', 'Lead times', 'Order quantities', 'Shipping times', 'Shipping carriers', 'Shipping costs']

# Drop rows with missing values
df.dropna(subset=features, inplace=True)

# Perform one-hot encoding for categorical variables
categorical_features = ['Product type', 'Availability', 'Customer demographics', 'Shipping carriers']
df_encoded = pd.get_dummies(df, columns=categorical_features)

# Split the data into training and testing sets
X = df_encoded.drop('Product Demand', axis=1)
y = df_encoded['Product Demand']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and fit the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model (e.g., using metrics like mean squared error)
mse = ((y_pred - y_test) ** 2).mean()
print('Mean Squared Error:', mse)

import matplotlib.pyplot as plt

# Scatter plot of actual vs predicted values
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Product Demand')
plt.ylabel('Predicted Product Demand')
plt.title('Actual vs Predicted Product Demand')
plt.show()


# import pickle

# # Assuming your trained model is stored in a variable named `model`
# with open('logisticRegression-model.pkl', 'wb') as file:
#     pickle.dump(model, file)
