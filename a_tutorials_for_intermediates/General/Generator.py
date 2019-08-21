"""
Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
Yeni sen bir istediyin kimi data generasiya edirsen funksiyanin komeyi ile sonra bu datani iterasiya edirsen.

"""


def counter():
    i=1
    while(i<=10):
        yield i     #instead of thte return statement
        i+=1

for i in counter():
    print(i)


def even(x):
    while x%2==0:
        yield 'Even'


#for i in even(2):
#    print(i)


def even_squares(x):
    for i in range(x):
        if i**2%2 == 0:
            yield i**2
print(list(even_squares(7)))

mylist=[1,3,6,10]
a=(x**2 for x in mylist)
print(next(a))
print(next(a))
print(next(a))
print(next(a))



