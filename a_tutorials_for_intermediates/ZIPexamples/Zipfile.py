from typing import List, Union
from zipfile import ZipFile
import datetime
import os

os.chdir("/home/babak/PycharmProjects/Linux/Tomcat/")
print(os.getcwd())
file = 'tomcat.zip'

with ZipFile(file, 'r') as zipone:                  # Zipfile constructur, READ mode
    zipone.printdir()                               #Show zip file content
    print("Extracting files")
    zipone.extractall()                             # Extract all content fo zip file
    print("Finsihed Extracting")
zipone.close()

# Extract single file from zip
with ZipFile(file, 'r') as zipone:
    zipone.extract('log.txt')
zipone.close()


