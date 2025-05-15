import pandas as pd
import numpy as np

# ---------------------------------------------
# Creating a sample DataFrame with missing values
# ---------------------------------------------
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4, 5],             # Column with a missing value
    'B': ['a', 'b', 'c', 'd', 'e'],        # Categorical column
    'C': np.random.randn(5),              # Normally distributed random values
    'D': np.random.randn(5)
})

print("🔹 Initial DataFrame:\n", df)

# ---------------------------------------------
# Descriptive Statistics using describe()
# ---------------------------------------------
# Automatically summarizes count, mean, std, min, quartiles, max for numeric columns
print("\n📊 Descriptive Statistics (numeric only):\n", df.describe())

# For non-numeric (categorical) data
print("\n📊 Descriptive Statistics (including object types):\n", df.describe(include='all'))

# ---------------------------------------------
# Additional Summary Functions
# ---------------------------------------------
print("\n✅ Mean of each numeric column:\n", df.mean(numeric_only=True))
print("\n✅ Median of each numeric column:\n", df.median(numeric_only=True))
print("\n✅ Minimum value in each column:\n", df.min(numeric_only=True))
print("\n✅ Maximum value in each column:\n", df.max(numeric_only=True))
print("\n✅ Standard deviation of each column:\n", df.std(numeric_only=True))
print("\n✅ Variance of each column:\n", df.var(numeric_only=True))
print("\n✅ Correlation matrix:\n", df.corr(numeric_only=True))

# ---------------------------------------------
# Skewness and Kurtosis
# ---------------------------------------------
print("\n✅ Skewness of numeric columns:\n", df.skew(numeric_only=True))
print("\n✅ Kurtosis of numeric columns:\n", df.kurt(numeric_only=True))

# ---------------------------------------------
# Frequency Count for a Categorical Column
# ---------------------------------------------
print("\n📌 Frequency count of values in column 'B':\n", df['B'].value_counts())

# ---------------------------------------------
# Handling Missing Data
# ---------------------------------------------

# Check how many missing values per column
print("\n🚨 Missing values in each column:\n", df.isnull().sum())

# Fill missing values in column 'A' with its mean
mean_val = df['A'].mean()
df['A'].fillna(value=mean_val, inplace=True)
print(f"\n🛠️ Filled missing values in column 'A' with mean ({mean_val:.2f}):\n", df)

# If desired: Drop all rows with any missing values (optional)
# df.dropna(inplace=True)

# Or, drop rows only if column 'C' or 'D' has missing values
# df.dropna(subset=['C', 'D'], inplace=True)

# ---------------------------------------------
# Final DataFrame Summary
# ---------------------------------------------
print("\n✅ Final DataFrame:\n", df)

# ---------------------------------------------
# Summary of Covered Functions
# ---------------------------------------------
# - describe(), mean(), median(), min(), max()
# - std(), var(), corr(), skew(), kurt()
# - value_counts()
# - isnull(), fillna(), dropna()
