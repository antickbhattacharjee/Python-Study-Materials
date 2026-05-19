# Positional Arguments
def full_name(first, last):
    print("Full name:", first, last)
full_name("John", "Doe")

# Keyword Arguments
def full_name(first, last):
    print("Full name:", first, last)
full_name(last="Doe", first="John")

# Default Arguments 
def greet(name="Guest"):
    print("Hello", name)

greet()           # Hello Guest
greet("Alice")    # Hello Alice

# Variable-Length Arguments
# *args → multiple positional arguments
def add_all(*nums):
    print(sum(nums))
add_all(1, 2, 3, 4)   # 10

# **kwargs → multiple keyword arguments
def show_info(**data):
    for key, value in data.items():
        print(key, ":", value)
show_info(name="Tom", age=30, city="Hooghly")
