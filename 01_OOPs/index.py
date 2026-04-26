
print("Welcome to Object-Oriented Programming (OOP) in Python!")


## 2. What are Classes and Objects?

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
########################################################################################################

## 3. Instance vs Class/Static Variables
class Customer:
    total_customers = 0  # Class variable to keep track of the total number of customers created

    """ Blueprint/Template for creating customer objects """
    def __init__(self, name, email):
        self.name = name
        self.email = email
        Customer.total_customers += 1

    def display_info(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Email: {self.email}")


customer1 = Customer("Bob", "bob@mailinator.com")
customer2 = Customer("Alice", "alice@mailinator.com")
customer3 = Customer("Charlie", "charlie@mailinator.com")
customer4 = Customer("Diana", "diana@mailinator.com")

print(f"Total Customers: {Customer.total_customers}")
########################################################################################################
