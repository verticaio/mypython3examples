import sys

siyahi = [i for i in range(0, 10)]
try:
    for i in siyahi:
        print(int(i)/0)
except ZeroDivisionError as hata:
    print(hata)



i = 5
if type(i) is int:
    raise TypeError("Integer lan bu")


def meminfo():
    assert ('linux' in sys.platform)
    ac = open("/proc/meminfo")
meminfo()


try:
    for i in range(3):
        print(3 / i)
except:
    print("You divided by 0")


print("Exceptiong Handling \n ")

a, b = 1, 0
try:
    print('10' + 1012)
    print(a / b)
except Exception as msg:
    print(msg)

print("Exceptiong Handling \n ")

a, b = 1, 22
try:
    print(a / b)
    print('10' + 1012)
except (TypeError):
    print("Invalid Input")
except ZeroDivisionError:
    print("Zero")

"""
try:
    print(1/0)
except:
    raise
except:
    print("Raised exception caught")
finally:
    print("Okay")
"""

#a, b = int(input("Enter first number: \n")), int(input("Enter second number: \n"))
#if b == 0:
#    raise ZeroDivisionError


a, b = int(input("Enter first number: \n")), int(input("Enter second number: \n"))
try:
    if b == 0:
        raise ZeroDivisionError
except ZeroDivisionError:
    print("You divided by zero")
    print("Will this print?")

print('1' + 1)
