# closures, nested function, and nonlocal variables
"""
Closure global variableleri gizletmek uchun istifade olunur, bir methodlu class kimi basha duse bielrsen
As closures are used as callback functions, they provide some sort of data hiding. This helps us to reduce the use of global variables.
When we have few functions in our code, closures prove to be efficient way. But if we need to have many functions, then go for class (OOP).

"""

def outerfunc(x):
    def innerfunct():
        print(x)
    innerfunct()
func1 = outerfunc(7)
#print(func1)

# Python program to illustrate
# nested functions
def outerFunction(text):
    text = text
    def innerFunction():
        print(text)
    innerFunction()

if __name__ == '__main__':
    outerFunction('Hey!')


# Python program to illustrate
# closures
def outerFunction(text):
    text = text

    def innerFunction():
        print(text)

    return innerFunction  # Note we are returning function WITHOUT parenthesis

if __name__ == '__main__':
    myFunction = outerFunction('Closureeeee!')
    print(myFunction())
    myFunction()





