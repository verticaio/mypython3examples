import csv

rows = []
with open('vn2018gen.csv', 'r+') as file:
    reader = csv.reader(file)  # Read Object
    for row in reader:
        if "." in str(row[2]):
            rows.append(row)

a = 0
for i in rows:
    a = a + 1
    print(str(i[2]).strip(' '))
print(a)