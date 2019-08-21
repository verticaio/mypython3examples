"""
we will focus on instance objects in python, python object initialization, create object python, assigning one object to another object in python,
assigning attributes to an object on the fly, deleting an object in python with Python object examples and syntax
"""
# Everyhing is object on python
print(type(7))
a = [1,2,3]
print(type(a))

def test_f():
    print("kkkk")

print(test_f)

b=True
print(type(b))

class fruit:
    def __init__(self, color, shape):
        self.color = color
        self.shape = shape
    def sayhi(self):
        print(self.color, self.shape)

