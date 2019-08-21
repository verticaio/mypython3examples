#Converting Integers to Floats
int()
float()
str()

f = 57
print(float(f))
i = 456.34
d = 45.67
print(int(i) + int(d))
a = 5 / 2
print(float(a))
print(int(a))

#Convertion Strings
s = 12
s1 = str(12)
print("s1" + "5")
user = "Sammy"
lines = 50
print("Congratulations, " + user + "! You just wrote " + str(lines) + " lines of code.")
#For converting strings to Int and float you int adn float functionn
a = ['pull request', 'open source', 'repository', 'branch']
print(tuple(a))
t = ('pull request', 'open source', 'repository', 'branch')
print(list(t))


print("Byte Objects and Strings:\n")
# Python code to demonstate String encoding
 
# initialising a String 
a = 'babakpythindeveloper'
c = b'babakpythindeveloper'

encod = a.encode('ASCII')

if (encod==c) :
	print("Encoding succesfully")
else :
	print("Encoding unsuccesfully")


decod = c.decode('ASCII')
if (decod==a):
	print("Decoding  is succesfully")
else :
	print("Decoding isn't succesful")