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
