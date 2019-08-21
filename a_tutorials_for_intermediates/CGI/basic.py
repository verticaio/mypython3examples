#!/usr/bin/python

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Word - First CGI Program</title>')
print ('</head>')
print ('<body>')
print ('<h2>Hello Word! This is my first CGI program</h2>')
print ('</body>')
print ('</html>')



import os

print ("Content-type: text/html\r\n\r\n <br>");
print ("<font size=+1>Environments:</font><br>");
print(os.environ.keys())
for param in os.environ.keys():
   print ("<b>%20s</b>: %s<\br>" % (param, os.environ[param]))

#Enable Apache cgi
# https://code-maven.com/set-up-cgi-with-apache