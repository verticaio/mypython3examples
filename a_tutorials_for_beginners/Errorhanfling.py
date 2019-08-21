# Syntax error varsa senin codun umumiyyetle icra olunmur,
# TypeError Senin object typlerinin birinde problem var demekdir
# Use try except variants and handle errors
# try odurki esas kodu icra ele, except odurki eger bele error gelse onda mene bu sekilde xetani goster

# Burada her hansi xeta cixsa bele mene 2 ci returnu qaytar
def devide(a,b):
    try:
        return a/b
    except :
        return "Zero Division is meaningless"

print(devide(1,0))

# Burada ise ancaq zero division xetasini tutsa mene 2 ci return qaytar
def devide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Zero Division is meaningless"

print(devide(1,0))