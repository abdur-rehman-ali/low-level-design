
print("Welcome to Object-Oriented Programming (OOP) in Python!")


class Person:
    """ Blueprint/Template for creating person objects """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class where we assign actual values
person1 = Person("Alice", 20)
person1.greet()

print("-" * 50)
