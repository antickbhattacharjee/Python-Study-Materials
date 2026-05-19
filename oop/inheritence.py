# Inheritence using python
class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the Parent class
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the greet method of the Parent class
        return f"{parent_greeting} I am {self.age} years old."
# Example usage
parent = Parent("Alice")
child = Child("Bob", 10)
print(parent.greet())  # Output: Hello, I am Alice.
print(child.greet())   # Output: Hello, I am Bob. I am 10 years old.
