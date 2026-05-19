import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age": [22, 23, 24, 25],
    "Salary": [25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

plt.pie(df["Salary"], labels=df["Age"], autopct='%1.1f%%')
plt.title("Salary Distribution")

plt.show()