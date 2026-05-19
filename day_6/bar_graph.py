import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

colors = ["Red", "#9200FA", "Blue", "#00FAF2"]

plt.bar(categories, values, color=colors)

plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Colored Bar Graph')
plt.show()

