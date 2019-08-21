import os, subprocess
import shutil
from threading import Thread
#os module

print(os.getcwd())
os.popen('cp file.salam test')
os.system('cp test dunya')

#Using Python Threading Library
Thread(target=shutil.copy, args=['dunya', '2.txt']).start()


# Using Python Subprocess Module.Syntax
# subprocess.call(args, *, stdin=None, stdout=None, stderr=None, shell=False, timeout=None)
status = subprocess.call('cp dunya subprocess', shell=True)
print(status)
if status != 0:
    if status < 0:
        print("Killed by signal {status}")
    else:
        print("Command failed with return code {status}")
else:
    print("Successfully executed command")


# Checkout
#status=subprocess.check_output('copy 1.txt 2.txt',shell=True)


#Using Python Shutil Module - copyfile(),copy(),copy2(),copyfileobj

# shutil.copyfile(src_file, dest_file, *, follow_symlinks=True)
shutil.copyfile('dunya', '2.222txt')