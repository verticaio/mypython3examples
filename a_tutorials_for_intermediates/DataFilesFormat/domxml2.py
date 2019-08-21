from xml.dom.minidom import parse
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("Test2.xml")
breakfast = DOMTree.documentElement

if breakfast.hasAttribute(''):
    print('Root:', breakfast.getAttribute())

foods = breakfast.getElementsByTagName('food')

for food in foods:
    print("Food:")
    if food.hasAttribute(''):
        print(food.getAttribute(''))
    name = food.getElementsByTagName('name')[0]
    price = food.getElementsByTagName('price')[0]
    description = food.getElementsByTagName('description')[0]
    calories = food.getElementsByTagName('calories')[0]
    print("%s" % name.firstChild.data, '-', "%s" % price.firstChild.data)
    print("%s" % description.firstChild.data, "%s calories per serving" % calories.firstChild.data)
