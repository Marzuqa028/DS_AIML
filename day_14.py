# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 10:02:12 2026

@author: sumai
"""
# ==========================================================
# DAY 12 — FEATURE ENGINEERING COMPLETE SCRIPT
# ==========================================================

# ----------------------------------------------------------
# STEP 1 — Import Libraries
# ----------------------------------------------------------
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, MinMaxScaler, StandardScaler, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# ----------------------------------------------------------
# STEP 2 — Create Dataset (Salary Prediction Example)
# ----------------------------------------------------------
# In real projects: df = pd.read_csv("dataset.csv")

data = {
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12],
    "Education_Level": ["Bachelors","Masters","PhD","PhD","Bachelors","Masters",
                        "PhD","Masters","Bachelors","Masters","Bachelors","PhD"],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance"],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000]
}

df = pd.DataFrame(data)

# ----------------------------------------------------------
# TOPIC 1 — Inspect Dataset & Identify Feature Types
# ----------------------------------------------------------
print("\nDataset Info:")
print(df.info())

# Separate target variable
target = "Salary"

# Identify numerical & categorical columns
numerical_cols = ["Age", "Experience"]
categorical_cols = ["Education_Level", "Department"]

# ----------------------------------------------------------
# TOPIC 2 — ENCODING CATEGORICAL VARIABLES
# ----------------------------------------------------------
# Label Encoding → for ORDINAL categories (Education Level has order)
le = LabelEncoder()
df["Education_Level_Encoded"] = le.fit_transform(df["Education_Level"])

# One-Hot Encoding → for NOMINAL categories (Department has no order)
df = pd.get_dummies(df, columns=["Department"], drop_first=True)

# Drop original categorical column after encoding
df = df.drop("Education_Level", axis=1)

print("\nDataset after encoding:")
print(df.head())

# ----------------------------------------------------------
# Prepare Feature Matrix (X) and Target (y)
# ----------------------------------------------------------
X = df.drop(target, axis=1)
y = df[target]

# Train-Test Split BEFORE scaling (to avoid data leakage)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ----------------------------------------------------------
# BASELINE MODEL (Before Scaling & Polynomial Features)
# ----------------------------------------------------------
model = LinearRegression()
model.fit(X_train, y_train)
baseline_preds = model.predict(X_test)

baseline_score = r2_score(y_test, baseline_preds)
print("\nBaseline Model R² Score:", baseline_score)

# ----------------------------------------------------------
# TOPIC 3 — FEATURE SCALING
# ----------------------------------------------------------
# Standard Scaling (mean=0, std=1)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model on scaled features
scaled_model = LinearRegression()
scaled_model.fit(X_train_scaled, y_train)
scaled_preds = scaled_model.predict(X_test_scaled)

scaled_score = r2_score(y_test, scaled_preds)
print("Model Score After Scaling:", scaled_score)

# ----------------------------------------------------------
# TOPIC 4 — POLYNOMIAL FEATURES (Non-linear relationships)
# ----------------------------------------------------------
poly = PolynomialFeatures(degree=2, include_bias=False)

X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

# Train model on engineered features
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)

poly_score = r2_score(y_test, poly_preds)
print("Model Score After Polynomial Features:", poly_score)

# ----------------------------------------------------------
# FINAL COMPARISON
# ----------------------------------------------------------
print("\n===== PERFORMANCE COMPARISON =====")
print("Before Feature Engineering :", baseline_score)
print("After Scaling             :", scaled_score)
print("After Polynomial Features :", poly_score)

# ----------------------------------------------------------
# FINAL FEATURE MATRIX READY FOR ML PIPELINES
# ----------------------------------------------------------
print("\nFinal Feature Shape:", X_train_poly.shape)

print("\nFeature Engineering Completed Successfully!")
# ==========================================================


#task 1 The categorical Converter
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "CarID": [1, 2, 3, 4, 5, 6, 7, 8],
    
    "Brand": [
        "Toyota", "Honda", "Ford", "BMW",
        "Hyundai", "Toyota", "Ford", "Honda"
    ],
    
    "Transmission": [
        "Automatic", "Manual", "Automatic", "Manual",
        "Automatic", "Manual", "Automatic", "Manual"
    ],
    
    "Color": [
        "Red", "Blue", "Green", "Red",
        "Blue", "Green", "Red", "Blue"
    ],
    
    "EngineSize": [1.5, 1.2, 2.0, 3.0, 1.6, 2.2, 2.5, 1.8],
    
    "Price": [20000, 18000, 25000, 40000, 22000, 27000, 32000, 21000]
}

df = pd.DataFrame(data)

print("\nData Types:")
print(df.dtypes)

le = LabelEncoder()
df["Transmission_Encoded"] = le.fit_transform(df["Transmission"])

# One-Hot Encoding → for NOMINAL categories (Department has no order)
df = pd.get_dummies(df, columns=["Color"], drop_first=True)
df = df.drop("Transmission", axis=1)


#task 2 The Leveling Field
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler,MinMaxScaler

data = {
    "EmployeeID": [1,2,3,4,5,6,7,8,9,10],
    
    "Age": [22, 25, 28, 35, 45, 30, 40, 50, 29, 33],
    
    "Salary": [25000, 30000, 32000, 50000, 80000, 45000, 70000, 90000, 38000, 52000],
    
    "YearsExperience": [1, 2, 3, 10, 20, 7, 15, 25, 5, 8]
}

df = pd.DataFrame(data)
print("\nData Types:")
print(df.dtypes)

scaler = StandardScaler()
standardized_data = scaler.fit_transform(df[["Age", "Salary", "YearsExperience"]])
df_standardized = pd.DataFrame(standardized_data, columns=["Age", "Salary", "YearsExperience"])
print(df_standardized.head())

minmax = MinMaxScaler()
normalized_data = minmax.fit_transform(df[["Age", "Salary", "YearsExperience"]])
df_normalized = pd.DataFrame(normalized_data, columns=["Age", "Salary", "YearsExperience"])
print(df_normalized.head())

plt.figure()
sns.histplot(df["Salary"], kde=True)
plt.title("Salary Before Scaling")
plt.show()

plt.figure()
sns.histplot(df_standardized["Salary"], kde=True)
plt.title("Salary After Standardization")
plt.show()

#task 3 The Complexity Creator
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
np.random.seed(42)
Experience = np.arange(1, 16)
Salary = 2000 * (Experience ** 2) + np.random.randint(-5000, 5000, 15)
df = pd.DataFrame({
    "Experience": Experience,
    "Salary": Salary
})
print("\nDataset Preview:")
print(df.head())
X = df[["Experience"]]
y = df["Salary"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)
linear_preds = linear_model.predict(X_test)
linear_r2 = r2_score(y_test, linear_preds)
print("\nR² Score (Linear Model):", linear_r2)

poly = PolynomialFeatures(degree=2, include_bias=False)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)
poly_preds = poly_model.predict(X_test_poly)
poly_r2 = r2_score(y_test, poly_preds)
print("R² Score (Polynomial Model):", poly_r2)

print("\n===== PERFORMANCE COMPARISON =====")
print("Linear Model R²      :", linear_r2)
print("Polynomial Model R²  :", poly_r2)
