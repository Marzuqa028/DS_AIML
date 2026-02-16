# ==========================================================
# DAY 11 — EXPLORATORY DATA ANALYSIS (EDA) COMPLETE SCRIPT
# ==========================================================

# ----------------------------------------------------------
# STEP 1 — Import Required Libraries
# ----------------------------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve plot appearance
sns.set(style="whitegrid")

# ----------------------------------------------------------
# STEP 2 — Load / Create Dataset
# (In real projects: df = pd.read_csv("dataset.csv"))
# ----------------------------------------------------------
data = {
    "Age": [25,30,35,40,28,32,1,3,45,50,23,36,29,41,80,90],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000,35000,40000,45000,26000],
    "Experience": [1,3,7,10,2,5,15,20,1,8,4,12,5,3,7,4],
    "Department": ["IT","HR","IT","Finance","HR","IT","Finance","Finance","HR","IT","HR","Finance","HR","IT","Finance","Finance"],
    "Gender": ["M","F","M","M","F","F","M","M","F","F","M","F","M","F","F","M"]
}

df = pd.DataFrame(data)

# ----------------------------------------------------------
# TOPIC 1 — DATASET INSPECTION
# ----------------------------------------------------------

# View first and last rows
print("\nFirst 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

# Dataset shape
print("\nDataset shape (rows, columns):", df.shape)

# Data types and missing values
print("\nDataset info:")
print(df.info())

# Summary statistics for numerical columns
print("\nSummary statistics:")
print(df.describe())

# ----------------------------------------------------------
# TOPIC 2 — UNIVARIATE ANALYSIS
# Analyze ONE variable at a time
# ----------------------------------------------------------

# HISTOGRAM — Distribution of Age
plt.figure()
sns.histplot(df["Age"], kde=True)
plt.title("Age Distribution")
plt.show()

# HISTOGRAM — Distribution of Salary
plt.figure()
sns.histplot(df["Salary"], kde=True)
plt.title("Salary Distribution")
plt.show()

# BOXPLOT — Detect spread & outliers in Salary
plt.figure()
sns.boxplot(x=df["Salary"])
plt.title("Salary Boxplot")
plt.show()

# CATEGORICAL ANALYSIS — Frequency counts
print("\nDepartment counts:")
print(df["Department"].value_counts())

print("\nGender counts:")
print(df["Gender"].value_counts())

# Bar plot for categorical variable
plt.figure()
sns.countplot(x="Department", data=df)
plt.title("Department Distribution")
plt.show()

# ----------------------------------------------------------
# TOPIC 3 — BIVARIATE ANALYSIS
# Study relationship between TWO variables
# ----------------------------------------------------------

# SCATTER PLOT — Age vs Salary
plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

# SCATTER PLOT — Experience vs Salary
plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

# BOXPLOT — Salary by Gender
plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("Salary by Gender")
plt.show()

# BOXPLOT — Salary by Department
plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("Salary by Department")
plt.show()

# ----------------------------------------------------------
# TOPIC 4 — CORRELATION ANALYSIS
# ----------------------------------------------------------

# Correlation matrix (numerical columns only)
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

# HEATMAP — visualize correlations
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# ----------------------------------------------------------
# TOPIC 5 — OUTLIER DETECTION
# ----------------------------------------------------------

# Boxplot for Age
plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age Outliers")
plt.show()

# Boxplot for Experience
plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience Outliers")
plt.show()

# ----------------------------------------------------------
# FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.
# ----------------------------------------------------------

print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")

# ==========================================================
# END OF EDA SCRIPT
# ==========================================================

# Task 1 The Distribution Deep-Dive

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "HouseID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "City": [
        "New York", "Los Angeles", "Chicago", "New York", "Houston",
        "Chicago", "Houston", "New York", "Los Angeles", "Chicago",
        "Houston", "New York", "Chicago", "Los Angeles", "Houston"
    ],
    "PropertyType": [
        "Apartment", "Villa", "Apartment", "Condo", "Villa",
        "Apartment", "Condo", "Villa", "Apartment", "Condo",
        "Villa", "Apartment", "Villa", "Condo", "Apartment"
    ],
    "Area_sqft": [850, 2000, 1200, 950, 1800, 1100, 1300, 2100, 1000, 1400, 1900, 900, 2200, 1500, 1250],
    "Price": [
        200000, 850000, 300000, 250000, 750000,
        320000, 400000, 950000, 280000, 450000,
        800000, 230000, 1000000, 500000, 350000
    ]
}

df = pd.DataFrame(data)

print(df.head())
print("\nData Types:")
print(df.dtypes)

plt.figure()
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.show()
print("Skewness:", df["Price"].skew())
print("Kurtosis:", df["Price"].kurt())

plt.figure()
sns.countplot(x = "City",data = df)
plt.title("City Distribution")
plt.show()


#task 2 The Relationship Map
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "HouseID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    
    "City": [
        "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
        "New York", "Chicago", "Houston", "Los Angeles", "Phoenix",
        "New York", "Chicago", "Houston", "Los Angeles", "Phoenix"
    ],
    
    "PropertyType": [
        "Apartment", "Villa", "Condo", "Apartment", "Villa",
        "Condo", "Apartment", "Villa", "Condo", "Apartment",
        "Villa", "Condo", "Apartment", "Villa", "Condo"
    ],
    
    "SquareFootage": [
        800, 1500, 1200, 900, 1800,
        2000, 1100, 1600, 1400, 1000,
        2200, 1300, 1700, 1900, 1250
    ],
    
    "Price": [
        200000, 450000, 320000, 230000, 600000,
        650000, 300000, 500000, 420000, 280000,
        720000, 350000, 550000, 620000, 330000
    ]
}

df = pd.DataFrame(data)

print(df.head())
print("\nData Types:")
print(df.dtypes)

plt.figure()
plt.scatter(df["SquareFootage"],df["Price"])
plt.xlabel("Square Footage")
plt.ylabel("Price")
plt.title("Scatter plot")
plt.show()

plt.figure()
sns.boxplot(x = "City", y = "Price",data = df)
plt.title("Boxplot")
plt.show()

print("As SquareFootage increases, Price seems to increase.")


#task 3 The Pattern Finder
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "SquareFootage": [800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800, 3000],
    "Bedrooms":       [2,    2,    3,    3,    4,    4,    5,    5,    6,    6],
    "Bathrooms":      [1,    1,    2,    2,    3,    3,    4,    4,    5,    5],
    "GarageSize":     [1,    1,    1,    2,    2,    2,    3,    3,    3,    4],
    "Price": [
        200000, 250000, 300000, 380000, 450000,
        520000, 600000, 680000, 750000, 1500000  # Outlier
    ]
}

df = pd.DataFrame(data)

print(df.head())
corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

print("Bedrooms and Bathrooms have a correlation higher than 0.8.")


# HEATMAP — visualize correlations
plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

plt.figure()
sns.boxplot(df["Price"])
plt.title("Box plot")
plt.show()



