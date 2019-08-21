#!/usr/bin/python


print("Set-Cookie:UserID = XYZ;\r\n")
print("Set-Cookie:Password = XYZ123;\r\n")
print ("Set-Cookie:Expires = Tuesday, 31-Dec-2018 23:12:40 GMT")
print("Set-Cookie:Domain = www.tutorialspoint.com;\r\n")
print("Set-Cookie:Path = /perl;\n")



print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')