# 1
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Woof")

# 2
class Person:
    def role(self):
        print("Person")

class Student(Person):
    def role(self):
        print("Student")

# 3
class Vehicle:
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")

# 4
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        print("Cannot fly")
