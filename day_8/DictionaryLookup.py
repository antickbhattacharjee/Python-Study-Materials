data = {"name": "Antick", "age": 25, "city": "Kolkata"}

try:
    key = input("Enter key to search: ")
    print("Value:", data[key])
except KeyError:
    print("Key not found in dictionary.")
