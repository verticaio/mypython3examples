
#h = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
#or sh in sh :
  #print(sh)
"""
list = ['shark', 'cuttlefish', 'squid', 'mantis shrimp']
print(list)

tuple = ('salam',"necesen","dunya")
print(tuple)

dictionary = {'name':'Babak','lastname':'Mammadov','WorkPlace':'Cybernet'}
print(dictionary)
print(dictionary['lastname'])

#Variabled
int = 21312412
print(int - 9)
my_string = 'Hello, World!'
my_flt = 45.06
my_bool = 5 > 9 
my_list = ['item_1', 'item_2', 'item_3', 'item_4']
my_tuple = ('one', 'two', 'three')
my_dict = {'letter': 'g', 'number': 'seven', 'symbol': '&'}
print(my_bool)

x = 10
x = "sabir"
print(x)
x = y = z = 123
print("x= ",x)
print("y= ",y)
print("z= ",z)

k,m,l = "shark", 2.05, 15
print (k,m,l)

#Global or Local variables
#Global variables exist outside of functions. Local variables exist within functions.
glb_var = "global"
def var_function():
    lcl_var = "local"
    print(lcl_var)
    print(glb_var)

var_function()
print(glb_var)


for i in range(3,13):
    print(i,i*i,i*i*i)

for i in range(3,13):
    print("{:15} {:15} {:15}".format(i, i*i, i*i*i))
"""

###Enumerate() in Python
l1 = ["eat","sleep","smell"]
s1 = "geek"
obj1 = enumerate(l1)
obj2 = enumerate(s1)
print("Return Type:", type(obj1))
print(list(enumerate(l1)))
print(list(enumerate(s1)))
print(list(enumerate(s1,3)))



for ele in enumerate(l1):
	print(ele)
print()


for count,ele in enumerate(l1,100):
	print(count," ",ele)