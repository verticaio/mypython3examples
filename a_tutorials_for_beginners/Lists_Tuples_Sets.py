
evens = []
for i in range(10):
	if i % 2 == 0:
		evens.append(i)

print(evens)

li = [1, 2, 6]
print([elem*2 for elem in li if elem>1])

stack = ['a','b','c','d']
stack.append('e')
stack.append('f')
print(stack)
stack.pop()
print(stack)
stack.pop(0)


print(stack)
stack.remove('b')


queue = ['a', 'b', 'c', 'd']
queue.append('e')
queue.append('d')
#print(queue)

import copy 
l2 = copy.copy(queue)

#print(l2)
#print(dir(copy))

a = [1, 2, [3, 4]]
b = a
#b = tuple(b)
print(type(b))
a[1] = 103
print("A:", a)
print("B:", b)

print("Another variant: \n")
import copy
a = [1, 2, [3, 4]]
b = copy.deepcopy(a)
a[2][0] = 10
print(a)
print(b)

print("Another variant: \n")

a=5
b=a
a=8
print(a)
print(b)

x = [4,1]
x.sort()
print(x)
import bisect
bisect.insort(x,6)
bisect.insort(x,7)
print(x)


#x = [4, 1]
#x.sort()
#import bisect
#print



###################################################################################3
## Tuples
"""
t = (1 , 2 , 3)
print(t[2])
t1 = 2,3,4
print(t1)

singleton = (1, )
print((1,) * 5)

s1=(1,0)
s1 +=(12,23,34)
print(s1)
#Methods


tup =	(1,2,3,5,1,4,1,6,8,1)
print(tup.count(1))   # Hesablayirki ne qeder 1 istifade olunur
print(tup.index(5))   # Gosterirki 5 valuesi hansi indexsdedir



print ("interest of tuples")

d = dict([('jan', 1), ('feb', 2), ('march', 3)])
print(d['feb'])

(x,y,z) = ('a','b','c')
print(z)

(x,y,z) = range(3)
print(z)
 

print("Tuple  Unpacking:")
date = (1,2,3)
x , y , z = date
print(z)

print("Tuple can be use as swap function")

def swap (a,b):
	(b,a) = (a,b)
	print("a:",a,"b:",b)

a = 2
b = 3
print(swap(a,b))


t=(1,2)
print(len(t))

t = (1,2,3,4,5)
newt = t
print(newt)
str(t)
print("Saalm")
print(str(t))
print(max(t))
t = (1, 2, [3, 10])
t[2][0]=9
print(t)

print("Dicts is used key value")
d = {'first':'tests', 'second':[1,2]}
print("Dicts keys list:", d.keys())
print("Dicts values list:",d.values())
print(d['first'])
print(d.items())
#d.has_key('first')
print(d.get('first'))




### Sets
x = set("A Python Tutorial")
print(x)
print(type(x))
x = set(["Python","Perl","Ruby"])
print(x)
cities = set(("Paris", "Lyon", "London","Berlin","Paris","Birmingham"))
print(cities)
my_set = {1,2,3}
my_set = {1.0, "Hello", (1, 2, 3)}
print(my_set)


# set do not have duplicates
# Output: {1, 2, 3, 4}
my_set = {1,2,3,4,3,2}
print(my_set)

# set cannot have mutable items
# here [3, 4] is a mutable list
# If you uncomment line #12,
# this will cause an error.
# TypeError: unhashable type: 'list'

#my_set = {1, 2, [3, 4]}

# we can make set from a list
# Output: {1, 2, 3}
my_set = set([1,2,3,2])
print(my_set)

a = {}
print(type(a))
a=set()
print(type(a))


my_set = {1, 2}
my_set.add(3)
print(my_set)
my_set.update([5,6,4])
print(my_set)

my_set.discard(5)
print(my_set)
my_set.remove(6)
print(my_set)


my_set = set("HelloWorld")
print(my_set)

# pop an element
# Output: random element
print(my_set.pop())
my_set.clear()
print(my_set)
"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Ferqli ve birlesdirme emeliyyati UNION", A|B)

print(A.union(B))
print(B.union(A))

print("Ortaq Elements Interception emeliyyati:", A&B)
print(A.intersection(B))
print(B.intersection(A))

print("Birincide olub ikincide olmayan", A - B)
print("Ikincide  olub birincide olmayan", B - A)
A.difference(B)
B.difference(A)


print("Symmetric Difference", A ^ B)

#Set Membership Test

# initialize my_set
my_set = set("apple")

# check if 'a' is present
# Output: True
print('d' in my_set)


dic = {"A":1, "B":2}
print(dic.get("A"))
print(dic.get("B"))
print(dic.get("C","Not Found ! "))


#ChainMap
import collections
dic1 = {'a' : 1 , 'b' : 2 }
dic2 = {'b' : 3 , 'c' : 4 }
dic3 = {'f' : 7 }


chain = collections.ChainMap(dic1,dic2)
print("Print All Dictionars contents:", chain.maps)
print("Print All Dictionars contents keys: ", list(chain.keys()))
print("Print All Dictionars contents values:", list(chain.values()))
chain1 = chain.new_child(dic3)
print("Print All Dictionars contents:", chain1.maps)
print("Print All Dictionars contents keys: ", list(chain1.keys()))
print("Print All Dictionars contents values:", list(chain1.values()))

print("Value associated with b before reversing is : ", end="")
print(chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)
print ("Value associated with b after reversing is : ",end="")
print (chain1['b'])



from collections import OrderedDict
print("\nThis is Dict:\n")
d = {}
d['a'] = 1
d['c'] = 5
d['b'] = 2
d['d'] = 3

for key, value in d.items():
	print(key,value)
print("\nThis is ordered dict:\n")
od = OrderedDict()
od['a'] = 1
od['c'] = 2
od['b'] = 3
od['d'] = 4
for key, value in od.items():
	print(key,value)


print("Before:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)
 
print("\nAfter:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)

