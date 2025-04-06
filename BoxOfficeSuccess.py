import pandas as pd  # Used to load and explore spreadsheet data
import numpy as np   # Useful for computations
from sklearn.linear_model import LinearRegression  # For building and training the prediction model

# Import the dataset from the Excel file
excelData = pd.read_excel("HW 6 Data.xlsx")

features = excelData[['ProductionBudget', 'GenrePopularity', 'CastStarPower']]  # Independent variables
boxOfficeTarget = excelData['BoxOfficeRevenue']  # Dependent variable (what we want to estimate)

# Initialize the linear regression model and train it
model = LinearRegression()
model.fit(features, boxOfficeTarget)  # Fit the model using training data

# Display model summary
print("\n Linear Model Summary")
print(f"→ Intercept: {model.intercept_:.2f} million")
for label, weight in zip(features.columns, model.coef_):
    print(f"→ Weight for '{label}': {weight:.2f}")


# Estimate revenue for custom movie inputs
testInput = pd.DataFrame([[120, 8, 6]], columns=features.columns)

# Generate prediction
estimatedRevenue = model.predict(testInput)[0]

print("\n Prediction Result:")
print(f"Given the values - Budget: 120M, Genre Popularity: 8, Cast Star Power: 6")
print(f" Predicted Box Office Revenue: {estimatedRevenue:.2f} million")
