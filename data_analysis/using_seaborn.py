import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = {
    "Age": [22, 23, 24, 25],
    "Salary": [25000, 30000, 35000, 40000]
}

df = pd.DataFrame(data)
sns.barplot(x="Age", y="Salary", data=df)
plt.title("Seaborn Bar Plot")

plt.show()