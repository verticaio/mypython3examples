x = 7
import os

import pickle

f = open("abc.txt", 'r+b')

print(pickle.dump(x,f))

print(pickle.dumps(x))

f.seek(0)
pickle.load(f)


grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }
#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )
#Reverse
noserial_grades = pickle.loads(serial_grades)
print(serial_grades)
print(noserial_grades)