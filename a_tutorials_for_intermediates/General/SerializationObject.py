import pickle


class Animal:
    def __init__(self, number_of_paws, color):
        self.number_of_paws = number_of_paws
        self.color = color


class Sheep(Animal):
    def __init__(self, number_of_paws, color):
        Animal.__init__(self, number_of_paws, color)


mary = Sheep('9', 'White')

print(str.format("My sheep mary is {0} and has {1} paws", mary.color, mary.number_of_paws))

# Create Serialize object
my_pickled_mary1 = pickle.dumps(mary)
print("Would you like to see her pickled? Here she is!")
print(my_pickled_mary1)

# Write to file
binary_file = open('my_pickled_mary.bin', mode='wb')
my_pickled_mary2 = pickle.dump(mary, binary_file)
binary_file.close()

# Now, let's unpickle our sheep Mary creating another
dolly = pickle.loads(my_pickled_mary1)




# print(str.format("My sheep dolly is {0} and has {1} paws", dolly.color, dolly.number_of_paws))



dolly.color = "black"
dolly.number_of_paws = 9
print(str.format("Dolly is {0} , {1}", dolly.color, dolly.number_of_paws))
print(str.format("Mary is {0} , {1} ", mary.color, mary.number_of_paws))