# Constructors and Destructors in Python

class SampleClass:
    def __init__(self, value):
        """Constructor method called when an object is created."""
        self.value = value
        print(f"Object created with value: {self.value}")

    def __del__(self):
        """Destructor method called when an object is about to be destroyed."""
        print(f"Object with value {self.value} is being destroyed.")
# Creating an object of SampleClass
obj = SampleClass(10)
print(f"Current value is: {obj.value}")