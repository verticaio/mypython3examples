from typing import List, Union
from zipfile import ZipFile
import datetime
import os

os.chdir("/home/babak/PycharmProjects/Linux/Tomcat/")
print(os.getcwd())
file = 'tomcat.zip'

with ZipFile(file, 'r') as zip:
    for info in zip.infolist():
        print(info.filename)
        print('\tModified:\t' + str(datetime.datetime(*info.date_time)))
        print('\tSystem:\t\t' + str(info.create_system) + '(0=Windows,3=Unix)')
        print('\tZIP version:\t' + str(info.create_version))
        print('\tCompressed:\t' + str(info.compress_size) + ' bytes')
        print('\tUncompressed:\t' + str(info.file_size) + ' bytes')
    zip.close()
