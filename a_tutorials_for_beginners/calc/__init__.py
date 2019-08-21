import calc
import exam
import builtins

from calc import div as d,floordiv as fd
from calc import *

d(10, 50)
fd(22, 44)

print(calc.__name__)

add = calc.add
print(add(5.5, 4))
print(type(add))

print(calc.mul(5, 8))

print(exam.show(123123123))

#Show build in modules
print(dir(builtins))
#Show you created module functions
print(dir(calc))