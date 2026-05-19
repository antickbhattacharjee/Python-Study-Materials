# Polymorphism using python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
class Cow(Animal):
    def speak(self):
        return "Moo!"
# Create instances of the classes
dog = Dog()
cat = Cat()
cow = Cow()
# Call the speak method on each instance
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print(cow.speak())  # Output: Moo!
# Polymorphism with a function
def animal_sound(animal):
    print(animal.speak())
# Call the function with different animal instances
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
animal_sound(cow)  # Output: Moo!
