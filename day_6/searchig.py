numbers=[3,6,9,2,7]
numbers.sort()
print("Sorted numbers:", numbers)
key = int(input("Enter a number to search: "))
for i in range(len(numbers)):
    if numbers[i] == key:
        print(f"Number {key} found at index {i}.")
        break
else:
    print(f"Number {key} not found in the list.")

fruits = ["apple", "banana", "cherry", "date"]
key_fruit = input("Enter a fruit to search: ")
for item in fruits:
    if item == key_fruit:
        print(f"{key_fruit} found at index {fruits.index(item)}.")
        break
else:
    print(f"Fruit '{key_fruit}' not found in the list.")