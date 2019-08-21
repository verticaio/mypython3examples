import os
print("Print current directory", os.getcwd())
print(type(os.getcwd()))
print("To get it as a bytes object", os.getcwdb())
print("Changing Current Python Directory")
os.chdir('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash/')
print("Print current directory", os.getcwd())
print("Python List Directories and Files", os.listdir())
print("Create Python directory")
#os.mkdir('TEST')
#os.rename('TEST', 'Babababb')
os.chdir('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash/Babababb/')
print(os.listdir())
#remove empty directory
#os.rmdir('dsad')
#Remove file
#os.remove('readmt.txt')

#Joining and Splitting Path


#Checking if Python Directory Exists
print(os.path.exists('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash/Babababb/'))

# Recursively Traversing a Directory in Python
for Babababb, apache,  ntp in os.walk('/home/babak/Desktop/Cybernet/Cybernet/Scripts/Bash/'):
    print(Babababb, len(apache), len(ntp))