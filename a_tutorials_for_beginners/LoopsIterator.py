from __future__ import print_function
import sys
# Program to find the sum of all numbers stored in a list
""""
s = 0
nums = [6, 5, 3, 8, 4, 2, 5, 4, 11]
for i in nums:
    s = s + i
print("Sum of nums:", s)

s = 0
for i in range(10):
    s = s + i
print("Sum of nums:", s)

print(list(range(5)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("Iterate over list also it is music type:",genre[i])

digits = [1, 2 , 3 ]
for i in digits:
    print(i)
else:
    print("No items left")
#What is reason of that


#While loop serti dogru olana qeder yoxlayir

n = 10
sum = 0
i = 1
while i <= 10:
    sum = sum + i ;
    i = i + 1

print("Show While Sum:", sum)


counter  = 0
while counter < 5:
    print("Inside While Loop")
    counter +=1
else:
    print("Out of the Loop")

#Break, continue, pass statement

counter  = 0
while counter < 5:
    print("Inside While Loop")
    counter +=1
    if counter == 3:
        print("I am using \"break\" statement when counter is 3 value")
        break

else:
    print("Out of the Loop")


for i in "strings":
    if i == "i":
        continue
    print(i)

print("The End")

sequence = {'p','a','c','d'}
for i in sequence:
    pass
print("Pass")


def function(args):
    pass
class example:
    pass




# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s :
    print(i)

# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d :
    #print(i,d[i])
    print("%s  %d" %(i, d[i]))

print("I am %s and I have %d galleons in my Gringotts bank account!" %('Harry Potter', 24));


# Nested loops


for i in range(1,6):
    print(i, end=" ")

"""

a = range(1,10)
print("The size allocated using range() is : ", sys.getsizeof(a))

def pypart(n):
    for i in range(0,n):
        







