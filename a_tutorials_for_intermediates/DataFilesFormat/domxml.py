from xml.dom.minidom import parse
import xml.dom.minidom
import os

os.chdir("/home/babak/PycharmProjects/OOP/DataFilesFormat/")
DOMTree = xml.dom.minidom.parse("Test.xml")
genre = DOMTree.documentElement


if genre.hasAttribute('catalogue'):
    print('Root:', genre.getAttribute("catalogue"))

songs = genre.getElementsByTagName('song')

for song in songs:
    print('Song:')
    if song.hasAttribute('title'):
        print(song.getAttribute('title'))
    artist = song.getElementsByTagName('artist')[0]
    year = song.getElementsByTagName('year')[0]
    album = song.getElementsByTagName('album')[0]
    print("Artist:", artist.firstChild.data)
    print("Year:", year.firstChild.data)
    print("Album:", album.firstChild.data)




