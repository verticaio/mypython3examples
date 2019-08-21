import threading
from queue import Queue
import time

def testThread(num):
	print(num)

if __name__ == '__main__':
	for i in range(5):
		t = threading.Thread(target=testThread(i))
		t.start()

exit()

## Run another command shell,cmd
import os
status = os.system('script2.py')
print ("exit status",status)


## Run a process and read its output as a file for example:
import os
for line in os.popen('ps aux').readlines():
	print(line)