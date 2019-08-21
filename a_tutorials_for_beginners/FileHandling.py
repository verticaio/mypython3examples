import os

print("Show current directory:", os.getcwd())
os.chdir('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash')
print("Sow current directory:", os.getcwd())
# Python File Methods
todo = open('test.txt', 'r+')
#detach ayirir binary buffer from TextIOBase and returns it
print(todo.detach())
print("\n \n ")
todo = open('test.txt', 'r+')
print(todo.read())
#fileno() returns a file descriptor of the file. This is an integer number.
print(todo.fileno())
todo1 = open('Ntp.sh', 'r+')
print(todo1.fileno())
todo2 = open('vsftpd.conf', 'r+')
print(todo2.fileno())
#flush() writes the specified content from the program buffer to the operating system buffer in event of a power cut.
todo.flush()
print("\n \n ")
#isatty()  This method returns True if the file is connected to a tty-like device.
print(todo.isatty())


#readable() in Python
print(todo.readable())
# Check file writeable or no
print(todo.writable())
#writelines() writes a list of lines to a file.
todo.writelines(['\nOne', '\nTwo', '\nThree'])
print(todo.read())