import os

print("Sow current directory:", os.getcwd())
print("Change default directory to /home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash ",
os.chdir('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash'))
print("List current dreictory:", os.listdir())
new1 = open('binary.txt', 'r+b')
new2 = open('binary.txt', 'a')
todo = open('test.txt', mode='r', encoding='utf-8')
# Read File
new1.read()
todo.read()
# Close File
todo.close()
new1.close()
new2.close()
"""
print("\n \n ")

try:
    f = open("test.txt", 'r+')
    print("Before")
    print(f)
    print(1 / 0)
except ZeroDivisionError:
    print("You don't divide by zero")
finally:
    f.close()




print("\n \n ")

with open('test.txt') as d:
    print(d.read(13))
    print(d.read())
    d.close()

with open('test.txt') as d:
    print(d.read(13))
    print("Tell,indiye qeder fayldaki son xarakerin nomresini deyir", d.tell())
    print("SEEK, yeni bu reqemden sonraki xaraktyerleri gosterir", d.seek(7))
    print(d.read())
    d.close()


print("FOR for TEXT")
for line in open('test.txt'):
    print(line, end='SSSS')
#end='' bu parametr her defe setri oxuyub verdikden sonra bir bosluq  vermesin deyedir

print("\n \n")
#readline read row by row
todo = open('test.txt')
print(todo.readline())
print(todo.readline())
print(todo.readline())
print(todo.readline())

print("\n  SSSSSSs \n")
#Lastly, the readlines() method reads the rest of the lines/file.
print(todo.seek(0))
print(todo.read(5))
print(todo.readlines())
"""
#Write File
a = open('test.txt', 'r+')
print(a.read())
a.write("\n HI")
print(a.read())
#a.close()