# Example of encapsulation using python
class Car:
    def __init__(self, make, model, year):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute
        self.__year = year  # Private attribute

    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

# Creating an object of Car class
my_car = Car("Toyota", "Corolla", 2020)
# Accessing private attributes using getter methods
print(f"Make: {my_car.get_make()}")
print(f"Model: {my_car.get_model()}")
print(f"Year: {my_car.get_year()}")
# Modifying private attributes using setter methods
my_car.set_year(2021)
print(f"Updated Year: {my_car.get_year()}")

