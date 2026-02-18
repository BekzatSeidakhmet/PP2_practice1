# 1
class A:
    pass

class B:
    pass

class C(A, B):
    pass

# 2
class Walker:
    def walk(self):
        print("Walking")

class Swimmer:
    def swim(self):
        print("Swimming")

class Amphibian(Walker, Swimmer):
    pass

# 3
class Writer:
    pass

class Speaker:
    pass

class Person(Writer, Speaker):
    pass

# 4
class Flyable:
    pass

class Runnable:
    pass

class SuperHero(Flyable, Runnable):
    pass
