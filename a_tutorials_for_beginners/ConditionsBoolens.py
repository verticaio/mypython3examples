# Comparision
# Object Identity : is
#  and
#  or
#  not


if True:
	print("Contditions was true:")


if False:
	print("Contditions was false:")


lang = "java"
if lang == 'python':
	print("Language is python")
elif lang == 'java':
	print("Language is Java")
elif lang == 'c#':
	print("Language is c#")
else:
	print("No match")

user = 'Admin'
logged_in = False
if user == 'Admin' or  logged_in:
	print("Admin Page")
else:
	print("Bad Creds")



if not logged_in:
	print("Please Log in")
else:
	print("Welcome")

a = [1,2,3]
b = [1,2,3]

print(id(a))
print(id(b))
print(a is b)


num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
#print("This is also always printed.")

#Nested IF
num  = float(input("Enter number: "))
if num >= 0:
	if num == 0:
		print("Zero")
	else:
		print("Positive Num")
else:
	print("Negative Number")