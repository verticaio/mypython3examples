A = [['Roy',80,75,85,90,95],['John',75,80,75,85,100],['Dave',80,80,80,90,95]]
w,h = 8,5;
Matrix = [[x for x in range(w)] for y in range(h)]
print(Matrix)
print(Matrix[1][3])


cars = ["Aston","Audi","Mclaren"]
for i, x in enumerate(cars):
    print(i," ", x)
cars = ["Aston","Audi","Mclaren"]
for i, x in enumerate(cars,start=5):
    print(i," ", x)

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS kit", "Car repair-tool kit"]

prices = {1:"570000$",2:"680000$",3:"450000$",
          4:"890000$", 5:"4500$"}

for index,c in enumerate(cars,start=1):
    #print("----", index,c)
    print("Car:%s Price: %s" %(c,prices[index]))

for index,c in enumerate(accessories,start=4):
    #print(index,c)
    print("Accessories:%s Price :%s" %(c,prices[index]))

"""
Car: Aston Price: 570000$
Car: Audi Price: 68000$
Car: McLaren Price: 450000$
Accessory: GPS kit Price: 890000$
Accessory: Car repair-tool kit Price: 4500$
"""

# Python program to demonstrate working of zip

# Two separate lists
cars = ["Aston", "Audi", "McLaren"]
accessories = ["GPS", "Car Repair Kit",
               "Dolby sound kit"]

# Combining lists and printing, Zip function combine same type data structure
for c, a in zip(cars, accessories):
    #print(c,a)
    print("Car: %s, Accessory required: %s" %(c, a))

