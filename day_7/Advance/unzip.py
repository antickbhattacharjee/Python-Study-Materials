combined = {"Alice": 25, "Bob": 30, "Charlie": 35}

names, ages = zip(*combined.items())
print(type(names))
print(type(ages))
