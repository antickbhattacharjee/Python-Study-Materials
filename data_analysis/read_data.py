import pandas as pd

df = pd.read_csv("data.csv")

print(df)

# Explore data

print(df.head())       # first rows
print(df.tail())       # last rows
print(df.shape)        # (rows, columns)
print(df.columns)      # column names
print(df.info())       # data types and non-null counts
print(df.describe())   # statistics for numeric columns
print(df["Name"])       # single column
print(df[["Name", "Age"]])  # multiple columns
print(df[df["Age"] > 25]) # Data filtering
print(df.sort_values("Salary", ascending=False)) # Sort by Salary

# Statistics
print(df["Age"].mean())   # Average age
print(df["Salary"].median()) # Median salary
print(df["Age"].value_counts()) # Count of unique ages
