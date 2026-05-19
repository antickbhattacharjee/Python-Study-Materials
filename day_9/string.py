'''
s1 = "Hello"
s2 = "World"
print(s1,s2) # Hello World
print(s1+s2)      # Concatenation → "HelloWorld"
print(s1 * 3)             # Repetition → "HelloHelloHello"


# looping
for char in "Python":
    print(char)

name = "John"
age = 25
print("my name is", name, "my age is", age) # Comma separator
print(f"My name is {name} and I am {age} years old.")   # f-string
print("My name is {} and I am {} years old.".format(name, age))  # using .format()

a = "My name is John"
b=a[11:15:2]  #slicing
print(b)

a = "python"
print(a[-1::-1])    #reverse

print(a.startswith("My"))   # starts with
print(a.endswith("hn"))   # ends with
'''
# String Slicing
a = "My name is John"
print(a.split())    # split space wise
print(a.split("a"))    # split with a
