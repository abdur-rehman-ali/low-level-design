# 🐍 Object-Oriented Programming in Python — Interview Guide

A comprehensive Q&A reference for Python OOP concepts with code examples.

---

## Table of Contents
1. [What is OOP?](#1-what-is-oop)
2. [Classes and Objects?](#2-what-are-classes-and-objects)
3. [Benefits of using Classes and Objects?](#3-benefits-of-using-classes-and-objects)
4. [Instance and Class Variables?](#4-instance-vs-classstatic-variables)
5. [Instance V/S Class V/S Static methods?](#5-instance-vs-class-vs-static-methods)
6. [Encapsulation](#6-encapsulation)

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

## 3. Benefits of Using Classes and Objects

**Q: What are Benefits of Using Classes and Objects**

**A:**

- **Organization:** Group related data and functions together
- **Reusability:** Create multiple objects from one class
- **Encapsulation:** Hide internal details and protect data
- **Modularity:** Break complex systems into manageable pieces
- **Inheritance:** Create hierarchies and reuse code

## 4. Instance vs Class/Static Variables

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


## 5. Instance vs Class vs Static Methods

**Q: What are the differences between Instance , Class and Static Methods**

**A:**
 
| Feature | Instance Method | Class Method | Static Method 
|---------|-----------------|--------------|---------------
| **Decorator** | None | `@classmethod` | `@staticmethod` 
| **First parameter** | `self` | `cls` | None |
| **Can access instance attributes** | ✅ Yes | ❌ No | ❌ No |
| **Can access class attributes** | ✅ Yes (via `self.__class__`) | ✅ Yes (via `cls`) | ❌ No (would need class name) | 
| **Can modify class state** | ✅ Yes (via `self.__class__`) | ✅ Yes (via `cls`) | ❌ No |
| **Called on** | Instance | Class or instance | Class or instance |
| **Use case** | Operations on instance data | Factory methods, modifying class state | Utility functions, grouping related functions |
 
---


## 6. Encapsulation

**Q: What is encapsulation? Key Characteristics of encapsulation? What are access modifiers?**

**A:**

Encapsulation is a fundamental Object-Oriented Programming (OOP) concept that bundles data (attributes) and methods that operate on that data within a single unit (class), while restricting direct access to some of an object's components


**Key Characteristics of Encapsulation:**

- **Data Hiding:** Prevent direct access to internal data
- **Controlled Access:** Provide public methods to access/modify private data
- **Protection:** Prevent accidental or unauthorized modification
- **Abstraction:** Hide complex implementation details


Python uses naming conventions:

| Convention | Prefix | Meaning |
|---|---|---|
| Public | `name` | Accessible anywhere |
| Protected | `_name` | Convention — don't access outside class/subclasses |
| Private | `__name` | Name-mangled — harder to access externally |

