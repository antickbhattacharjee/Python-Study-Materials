import pandas as pd

# Create sample data
data = {
    "Name": ["Amit", "Sara", "John", "Riya"],
    "Age": [23, 25, 22, 24],
    "Salary": [30000, 40000, 25000, 35000]
}

df = pd.DataFrame(data)

# Show data
print(df)
print(df.head())        # first 5 rows
print(df.info())        # data info
print(df.describe())    # statistics
print(df.drop("Age", axis=1))  # drop column
for col in df["Age" > 60]:
    df.drop(col, inplace=True)  # drop rows based on condition

print(df["Name"])        # single column
print(df[["Name", "Salary"]])  # multiple columns
print(df[df["Salary"] > 30000]) # Data filtering
print(df[(df["Salary"] > 30000) & (df["Age"] < 25)]) # Data Double filtering
df["Bonus"] = df["Salary"] * 0.10 # Add new column
print(df)
