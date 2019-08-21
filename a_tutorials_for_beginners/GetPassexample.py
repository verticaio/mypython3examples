
import getpass
try:
    p = getpass.getpass(prompt='Enter Password: ', stream=None)
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)


user = getpass.getuser() 
  
while True: 
    pwd = getpass.getpass("User Name : %s" % user) 
  
    if pwd == 'abcd': 
        print("Welcome!!!")
        break
    else: 
        print("The password you entered is incorrect.")