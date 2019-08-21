#strings

print("Sammy" + "Babak")
print("Sammy" + "27" )

#Format Text

a = 'Sammy says, "Hello!"'
print(a)

b = '''
This string is on 
multiple lines
within three single 
quotes on either side.
'''
print(b)

print("1.\tShark\n2.\tShrimp\n10.\tSquid")

#Raw strings
print(r"Sammy says,\"The balloon\'s color is red.\"")


#Index,Slicing Strings
ss = "Sammy Shark!"
print(ss[0],ss[11])
#Negative indexing sure 0 yoxdur 1 den bashlayir
print(ss[-5],ss[-1],ss[-12])
print(ss[::4])

message="Hello's World Salam Necesen"
length=len(message)
print("Message metninin uzunlugu:",length,"xarakterden ibaretdir")
print(message[0])
print(message[0:9])
print(message[:5])
print(message[6:])


#String methods
#F strings

movie = "2001: A SAMMY ODYSSEY"
book = "A Thousand Splendid Sharks"
poem = "sammy lived in a pretty how town"
balloon = "Sammy has a balloon."
print(movie.islower())
print(movie.isupper())
print(book.istitle())
print(book.isupper())
print(poem.istitle())
print(poem.islower())
message="Hello's World Salam Necesen"
length=len(message)
print("Message metninin uzunlugu:",length,"xarakterden ibaretdir")
print(message[0])
print(message[0:9])
print(message[:5])
print(message[6:])
print(message.lower()) 
print(message.upper())
print("Message Sozunde ne qeder Hello ishlenib",message.count("Hello"))
print("Message Sozunde ne qeder l ishlenib",message.count("l"))
print("Message Sozunde World sozunun basladigi yeri gosterir",message.find("World"))
print(message.replace("Salam","Necesen"))
greeting = 'Hello'
name = 'Country'
message = greeting + ' , ' + name + '. Welcome!'
print(message)
message_new = '{} , {} . Great'.format(greeting,name)
print(message_new)

#F sting examples
message_new_f = f'{greeting}. {name} , Test!'
print(message_new_f)
message_new_f_1=f'{greeting.upper()}'
print(message_new_f_1)
#Show string methods and manual
print(dir(name))
print(help(str))
print(help(str.upper))

#String Formatters 
print("Babak have {} old ".format(23))

open_string = "Sammy Loves {}"
print(open_string.format("Babalk"))
new_open_string = "Sammy loves {} {}."                   
print(new_open_string.format("open-source", "software"))   
#Reordering Formatters with Positional and Keyword Arguments


print("Salam menim {2} yashim var. {0} sirketinde {1} ildiki ishleyirem".format("Cybernet", 2, 23))


print("Sammy  the {0} {1} a {pr}.".format("ddd","dadsad", pr =  "salam" ))
print("Sammy ate {0:f} percent of a {1}!".format(75, "pizza"))
print("Sammy ate {0:.0f} percent of pizza".format(75.23432423))
#Padding Variable Substitutions
print("Sammy has {0:0} red {1:50}!".format(5, "balloons"))




# Python program to demonstrate the use of formatting using %
  
# Initialize variable as a string
variable = '15'
string = "Variable as string = %s" %(variable)
print(string)
  
# Printing as raw data
# Thanks to Himanshu Pant for this
print("Variable as raw data = %r" %(variable))
  
# Convert the variable to integer
# And perform check other formatting options
  
variable = int(variable) # Without this the below statement
                        # will give error.
string = "Variable as integer = %d" %(variable)
print(string)
print("Variable as float = %f" %(variable))

# printing as any string or char after a mark
# here i use mayank as a string
print ("Variable as printing with special char = %cmayank" %(variable))
 
print("Variable as hexadecimal = %x" %(variable))
print("Variable as octal = %o" %(variable))

from string import Template
t = Template('x is $x')
# Substitute value of x in above template
print(t.substitute({'x' : 1}))

# List Student stores the name and marks of three students
Student = [('Ram',90), ('Ankit',78), ('Bob',92)]
t = Template('Hi $name, you have got $marks marks')

for i in Student:
	print(i)
	print(i[0])
	print(i[1])
	print(t.substitute(name = i[0], marks = i[1]))




