#User-Define, Built-in,lambda ,Recursion Functions






#all,any,bytes,bytearry,hasattr ?
input("Enter number:")
print(callable([1,2,3]))
print(callable(callable))
print(chr(65))
x=7
print(eval('x+7'))
exec('a=2;b=3;print(a+b)')
print(hash('babak'))

def func1(a):
    if a%2==0:
        return 0
    else:
        return 1

print(func1(7))

def sum1(a,b):
    return a+b
print(sum1(12,7))

def hello():
    """
    This is docstring
    This is test, for calling doc string fo the func you have to use print(funcname.__doc__)
    """
    print("Calling Function hello(), Heyyyyyyyyyy:")


hello()
print(hello.__doc__)
print(type(hello.__doc__))

sum.__doc__
print(type(sum.__doc__))
print(bool(sum.__doc__))

def hello1():
    pass
hello1()


def sum(a,b):
    print(f"{a}+{b}={a+b}")
    print(a,"+",b,"=",a+b )

sum(5,7)

def func2():
    c=0
    c+=1
    print(c)

func2()

print("Echooooooooooooooo:",func1(7))
del func1
#print(func1(7))






############################
#Lambda expressions --- a function doesn’t need to have a name. A lambda expression in Python allows us to create anonymous python functions we use the ‘lambda’ keyword for it
myvar = lambda a,b:(a*b)+12
print(myvar(3,5))
double = lambda x: x * 2
print(double(3))


#use lambda with filter functions
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0),my_list))
print(new_list)

# use lambda map functions
map_list = list(map(lambda x: x * 2,my_list))
print(map_list)

#Python Recursion(Oz ozunu cagirma, Tekrarlanma)
def facto(n):
    if n==1:
        return 1
    return n * facto(n-1)
print(facto(5))

def countdown(i):
  print(i)
  # base case
  if i <= 0:
    return
  # recursive case
  else:
    countdown(i-1)

countdown(5)


############################
## Bult in examples
#any,all ?
print("Python Built-in Functions:")
c = abs(-7)
print(c)



print(ascii('uşor'))

#Let’s apply it to a list.
print(ascii(['s','ș']))


print(" bin() converts an integer to a binary string:", bin(3))

print(bool(0.5))
print(bool(''))

a=bytearray(4)
print(a)
a.append(1)
print(a)
a[0]=1
print(a)
print(bytes('hello','utf-8'))
#oth bytes() and bytearray() deal with raw data, but bytearray() is mutable, while bytes() is immutable.


