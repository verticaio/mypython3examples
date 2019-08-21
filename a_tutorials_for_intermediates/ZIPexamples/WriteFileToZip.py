from zipfile import ZipFile
import os

def get_paths(directory):
    paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            #print("ROOT:",root, "Directories:", directories, "Files:", files)
            paths.append(filepath)
    return paths

paths = get_paths('./TEST')
print("Zipping these files")
for file in paths:
    print(file)

with ZipFile('tomcat.zip', 'w') as zipwri:
    for file in paths:
        zipwri.write(file)
    print("Zip Succesfully")
    zipwri.printdir()
zipwri.close()
