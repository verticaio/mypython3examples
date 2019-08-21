### Search for pysftp
# $ pip search pysftp
# $ pip install pysftp
#### Parameter	Description
#host	 	The Hostname of the remote machine.
#username	Your username at the remote machine.(None)
#private_key	Your private key file.(None)
#password	Your password at the remote machine.(None)
#port	 	The SSH port of the remote machine.(22)
#private_key_pass password to use if your private_key is encrypted(None)
#log	 	log connection/handshake details (False)

import pysftp
srv = pysftp.Connection(host="your_FTP_server", username="your_username",
password="your_password")
# Get the directory and file listing
data = srv.listdir()
# Closes the connection
srv.close()
# Prints out the directories and files, line by line
for i in data:
    print i


import pysftp
import sys
# Defines the name of the file for download / upload
remote_file = sys.argv[1]
srv = pysftp.Connection(host="your_FTP_server", username="your_username",
password="your_password")
# Download the file from the remote server
srv.get(remote_file)
# To upload the file, simple replace get with put. 
srv.put(remote_file)
# Closes the connection
srv.close()


import pysftp as sftp
def sftpExample():
	try:
		s = sftp.Connection('ftp.company.com', username='enterusername', password='enterpassword')
		remotepath1='/home/filepath/sample.xlsx'
		localpath1="\\\\corporatenetwork\\datapath\\sample.xlsx"
		s.get(remotepath1,localpath1, preserve_mtime=True)
		s.close()
	except Exception, e:
		print str(e)
sftpExample()





import pysftp

myHostname = "yourserverdomainorip.com"
myUsername = "root"
myPassword = "12345"

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
    print "Connection succesfully stablished ... "

    # Define the file that you want to upload from your local directorty
    sftp.remove('/var/custom-folder/TUTORIAL2.txt')
 
# connection closed automatically at the end of the with-block