# 🐍 Object-Oriented Programming in Python — Interview Guide

A comprehensive Q&A reference for Python OOP concepts with code examples.

---

## Table of Contents
1. [What is OOP?](#1-what-is-oop)
1. [Classes and Objects?](#2-what-are-classes-and-objects)


## 1. What is OOP?

**Q: What is Object-Oriented Programming and what are its four pillars?**

**A:** OOP is a programming paradigm that organizes code around **objects** (data + behavior) rather than functions and logic. The four pillars are:

| Pillar | Description |
|---|---|
| **Encapsulation** | Bundling data and methods, hiding internal state |
| **Inheritance** | A class derives properties/behavior from a parent class |
| **Polymorphism** | Different classes respond to the same interface differently |
| **Abstraction** | Hiding complexity, exposing only what's necessary |

---

## 2. What are Classes and Objects?

**Q: What is the difference between a class and an object?**

**A:**

**Class:** A blueprint or template for creating objects. It defines the properties (attributes) and behaviors (methods) that objects of that class will have.

**Object:** An instance of a class - a concrete entity created from the class blueprint with actual values.


```python
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
```


## 3. Instance vs Class/Static Variables

**Q: What are the differences between instance and class/static variables?**

**A:**

| Type | Scope | Shared? | Accessed via |
|---|---|---|---|
| Instance variable | Per object | No | `self.var` |
| Class variable | All instances | Yes | `ClassName.var` |

```python
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
```
