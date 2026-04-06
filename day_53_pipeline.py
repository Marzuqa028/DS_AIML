from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
import pandas as pd

# Sample Dataset 
data = pd.DataFrame({
    'numerical_column': [10, 20, 30, 40, 50],
    'categorical_column': ['A', 'B', 'A', 'B', 'C'],
    'target': [0, 1, 0, 1, 0]
})

X = data[['numerical_column', 'categorical_column']]
y = data['target']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Column Transformer
preprocessor = ColumnTransformer([
    ('num', StandardScaler(), ['numerical_column']),
    ('cat', OneHotEncoder(), ['categorical_column'])
])

# Pipeline
pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression())
])

# Train + Predict
pipeline.fit(X_train, y_train)
predictions = pipeline.predict(X_test)

print(predictions)