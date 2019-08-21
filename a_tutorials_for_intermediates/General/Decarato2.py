


def decor(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print("You don't devide by 0!")
        return func(*args, **kwargs)
    return wrapper

@decor

def divide(a, b):
    return a/b

print(divide(200,5))


"""
Eger sen yeni variable yaradib onu value oturmek istemirsense bucur yaza bilersen buna pie sytaxi deyilir
Yeni Burda ferq odurki mentiqi olaraq sen varibale olan  pie den sonra yaziras.Yeni bu asagidakini edir.

"""


def decor(func):
    def wrapper(*args, **kwargs):
        if args[1] == 0:
            print("You don't devide by 0!")
        return func(*args, **kwargs)
    return wrapper



def divide(a, b):
    return a/b
divide = decor(divide)

print(divide(200, 20))


