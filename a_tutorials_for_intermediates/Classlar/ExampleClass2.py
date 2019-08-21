class Fruit:
    """
    This Python3 class creates instances of fruits
    """
    color = 'Red'  # Atribute

    def sayhi(self):  # method to call on an object of class frui
        print('Hi')


obj2 = Fruit()
print(obj2.color)  # access the members of a class
print(obj2.sayhi())  # call of the method of class


class Try1:
    def mymethod(self):
        def sayhello():
            print('Hello')
            print("Hi")

        sayhello()


obj1 = Try1()
print(obj1.mymethod())


class Fruit2:
    def size(self, x):
        print("I am size %s" % x)


orange = Fruit2()
print(orange.size(10))
print(Fruit2.__doc__)


class Fruit3:
    def __init__(self, color,  size):
        self.color = color
        self.size = size
    def sal(self, agilliol):
        print("I am {0} and size {1}".format(self.color, self.size),  agilliol)

orange1 = Fruit3("Black", 8)
print(orange1.sal("Agilloolanlar"))

