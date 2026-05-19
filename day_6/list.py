
numbers = [10,1.2, "Hello", True]
a = [1,4,7,[5,6,8]]
print(a[3][1])

numbers.append(40)
numbers.insert(1, 15)
numbers.remove(20)
numbers.sort()
print(numbers)    # [10, 12, 15, 30, 40]

for i in range(len(numbers)):
    print(numbers[i])


key = int(input("Enter key: "))
if key not in numbers:
    print(f"{key} is not present in this list")

num2 = numbers.copy()
print(num2)
num3=["apple", "banana", "grapes"]
print(max(num3))
print(min(num3))

