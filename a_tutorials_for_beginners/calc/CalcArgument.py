import sys


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def exp(a, b):
    return a ** b


def floordiv(a, b):
    return a // b


if __name__=="__main__":
    print("command arguments:", sys.argv)

if int(sys.argv[1]) == 1:
    print(add(int(sys.argv[2]), int(sys.argv[3])))
elif int(sys.argv[1]) == 2:
    print(sub(int(sys.argv[2]), int(sys.argv[3])))
else:
    print("Output")