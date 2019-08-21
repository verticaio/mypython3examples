import os, sys
os.chdir("/home/babak/PycharmProjects/Linux/TEST")
print('We have:', os.listdir())
# os.rename('file.salam','dunya')


# Rename multiple files
i = 1
for file in os.listdir():
    src = file
    dst = "Dog" + str(i) + ".jpg"
    os.rename(src, dst)
    i += 1
