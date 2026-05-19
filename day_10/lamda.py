# lamda function
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# user input and lambda
multiply = lambda x, y: x * y
a, b = map(int, input("Enter two numbers separated by space: ").split())
print("The product is:", multiply(a, b))
print(f"{a}, {b}")
