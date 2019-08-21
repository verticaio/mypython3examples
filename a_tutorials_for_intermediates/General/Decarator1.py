def decor(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print("You don't devide by 0!")
        return func(*args, **kwargs)
    return wrapper

def divide(a, b):
    return a/b
test = decor(divide)  # Burda onu duzeldir, variableleri tanidir sonra sadece deyer oturmek qalir
print(test(20, 10))   # bunu bele yazanda o onceden test obyekti yaratdigi uchun bilir ki artiq deyerleri wrapper(20,10) kimi oturmek lazimdir


"""
Burdaki test(20, 10) 20 ve 10 hansiki nestende functiona oturulen arqumentlerdi yeni def wrapper(*args, **kwargs):
*args is a tuple of arguments, and **kwargs is a dictionary of keyword arguments.
"""


#Pie Syntax in Python


def decor1(func):
    def wrap():
        print("$$$$$$$$$$$$$$")
        func()
        print("$$$$$$$$$$$$$$")
    return wrap

def decor2(func):
    def wrap():
        print("##############")
        func()
        print("##############")
    return wrap

@decor1
@decor2
def sayhello():
    print("Hello")
sayhello()

#OLD
print("Old Style1111111111111111111")
a = decor1(sayhello)
a()

print("Old Style22222222222222222")
b = decor2(sayhello)
b()

