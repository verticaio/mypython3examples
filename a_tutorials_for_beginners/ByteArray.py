#COnvert bytes to integer to convert normal reqem find out in asciitable.com
a = "35 2e 36"
b = bytearray()
for i in a.split(" "):
    tmp = int("0x"+i,16)
    print(tmp)
    b.append(tmp)


print(b.decode())
