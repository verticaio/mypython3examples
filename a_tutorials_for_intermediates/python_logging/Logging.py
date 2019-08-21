import logging
from datetime import datetime, timedelta

logging.basicConfig(filename="file.log", level=logging.DEBUG, format = "%(asctime)s:%(levelname)s:%(message)s")


class Pizza():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        logging.debug("Pizza created : {} (${})".format(self.name, self.price))

    def make(self, quantity=1):
        logging.debug("Made {} {} pizza(s)".format(quantity, self.name))

    def eat(self, quantity=1):
        logging.debug("Ate {} pizza(s)".format(quantity, self.name))


pizza_01 = Pizza("artichoke", 15)
pizza_01.make()
pizza_01.eat()
pizza_02 = Pizza("margherita", 12)
pizza_02.make(2)
pizza_02.eat()

f = open("file.log", "a+")
f.write("\n{}:DEBUG:This is next class retrieve \n".format(datetime.now()))
f.close()