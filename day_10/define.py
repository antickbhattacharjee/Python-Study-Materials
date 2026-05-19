
# ✅ Defining and Calling a function
def greet():
    print("Hello, welcome to Python!")

greet()   # Calling the function

# 🔢 Function with Parameters
def add(a, b):
    result = a + b
    print("Sum is:", result)

add(5, 10)     # Output: Sum is: 15

# 🔙 Function with Return Value
def square(n):
    return n * n

result = square(4)
print("Square is:", result)    # 16

name = input("Enter your name: ")

def greet(name):
    print(f"Hello, {name}!")

greet(name)