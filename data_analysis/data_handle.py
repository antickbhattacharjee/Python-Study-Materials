import pandas as pd
# Load data
df = pd.read_csv("data.csv")

# handle missing and duplicate data
df = df.dropna()  # Remove rows with missing values
df = df.drop_duplicates()  # Remove duplicate rows
# Handle outliers (example: remove rows where Salary > 100000)
df = df[df["Salary"] <= 100000]
# Convert data types if necessary (example: convert Age to integer)
df["Age"] = df["Age"].astype(int)
# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)