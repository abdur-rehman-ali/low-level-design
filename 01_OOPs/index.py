
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
print("-" * 50)
########################################################################################################

class Employee:
    company = "Tech Corp"

    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Company: {Employee.company}")

    def change_company_instance(self, new_company):
        self.__class__.company = new_company
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

    @staticmethod
    def print_hello():
        print("Hello from the Employee class!")
    
    def __str__(self):
        return f"{self.name} - {self.position} at {Employee.company}"


employee1 = Employee("Eve", "Software Engineer")
employee1.display_info()
Employee.change_company("New Tech Corp")
employee1.display_info()
Employee.print_hello()
employee1.print_hello()
employee1.change_company_instance("Another Tech Corp")
employee1.display_info()
