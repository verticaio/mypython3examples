"""
Python Decorators funksiyadir ve basqa birine elave funksionnaliq  verir amma modify elemir.
Python Decorator wraps(tamamlayir) another function.It is also metaprogramming because a part of the program tries to modify another at compile time
This is useful in cases when you want to add functionality to a function
Umumiyyetle yadda saxla

def func():
    print(5)

Eger bele yazsan onda sene funksianin obyektini verecek
func
Yoxsa bele yazsan onda sene onun ichindeki datani verecek
func()
"""


def func():
    print(5)
func
func()

def decor(func):
    def wrap():
        print("$$$$$$$$$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$$$$$$$$$")

    return wrap


def sayhello():
    print("Hello")


dectest = decor(sayhello)
dectest()

print("Without nested functions")


def decor(func):
    print("$$$$$$$$$$$$$$$$$$$$$$")
    func()
    print("$$$$$$$$$$$$$$$$$$$$$$")

    def babak():
        print("Babak")

    return babak


def sayhello():
    print("Hello")


dectest = decor(sayhello)
dectest()
dectest = decor(sayhello)

print("Decorator")

def divide(a,b):
    return a/b

def dacarator(func):
    def wrapper(a,b):
        if b==0:
            print("You don't devide by 0!")
        return func(a,b)
    return wrapper

testdec = dacarator(divide)
print(testdec(10,5))




print("*args and  **kwargs")
"""
If you don’t want to type in the whole list of arguments for the two statements, *args and **kwargs will do the trick for you
"""
