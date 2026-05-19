# 1. Division
try:
    x = 10 / 0  # Division by zero
except ZeroDivisionError as e:
    print(f"Division Error: {e}")

# 2. Input conversion
try:
    num = int("abc")  # Invalid input conversion
except ValueError as e:
    print(f"Value Error: {e}")

# 3. List indexing
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Index out of range
except IndexError as e:
    print(f"Index Error: {e}")

# 4. Dictionary key access
my_dict = {"name": "Alice"}
try:
    print(my_dict["age"])  # Key not found
except KeyError as e:
    print(f"Key Error: {e}")

# 5. File reading
try:
    with open("non_existent_file.txt", "r") as f:
        data = f.read()  # File does not exist
except FileNotFoundError as e:
    print(f"File Not Found Error: {e}")

# 6. Math functions
import math
try:
    print(math.sqrt(-1))  # Invalid math operation
except ValueError as e:
    print(f"Math Error: {e}")
