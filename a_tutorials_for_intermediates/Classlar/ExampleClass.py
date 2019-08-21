class Car:
    def __init__(self, brand, model, color, fuel):
        self.brand = brand
        self.model = model
        self.color = color
        self.fuel = fuel

        def start(self):
            pass

        def halt(self):
            pass

        def drift(self):
            print("S")

        def speedup(self):
            pass

        def turn(self):
            pass
blackverna = Car('Hyundai', 'Verna', 'Black', 'Diesel')
print(blackverna.color, blackverna.fuel)


print("\nMethod Examples: \n")

class Try:
    def __init__(self):
        pass

    def printhello(self, name):
        print("Hello ,", name)
        return name

obj = Try()
obj.printhello('Ayushi')




# Class konstruktor(special function) classla eynu adda olmalidir and atributed example def __init.py. Bun init.py class
# atributlarini initialize etmek uchundur__. Eslinde sen bununteyin etmeyede bilersen
print("\nClass __init.py__ example constructor as special  function yeni method birinci method of class and bunun atributlari olur: \n")

class Animal:
    def __init__(self, species, gender):
        self.spe = species
        self.gen = gender

flufully = Animal('Dog', 'Male')
print(flufully.gen, flufully.spe)

class Try2:
    def hello(self):
        print("Method of class without __init.py__ I mean konstruktorsuz")

obj2 = Try2()
print(obj2.hello())




#Self example
class Fruit:
    def printstate(self, state):
        print("Oracge is ", state)
        return state
obj3 = Fruit()
print(obj3.printstate("Ripe"))

class Result:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    def printavg(self):
        print("Average=", (self.phy+self.chem+self.math)/3)   # Burada Method class daxilindeki data ile yeni atributlarla elaqeder oldu

cavab = Result(20, 30, 40)
print(cavab.printavg())


# Self parametrind adini nece isteyirsen qoya bierlsen bir class daxilinde
class Fruit2:
    def printstate2(lef, state):
        print("Oracge is ", state)
        return state
obj4 = Fruit2()
print(obj4.printstate2("Ripe"))