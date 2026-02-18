# 1
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

# 2
class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name):
        super().__init__(name)

# 3
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand):
        super().__init__(brand)

# 4
class Shape:
    def __init__(self, color):
        self.color = color

class Circle(Shape):
    def __init__(self, color):
        super().__init__(color)
