import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age": [22, 23, 24, 25],
    "Salary": [25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)

plt.plot(df["Age"], df["Salary"])
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs Salary")

plt.show()