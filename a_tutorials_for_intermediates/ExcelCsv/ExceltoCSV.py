import xlrd
import csv
book = xlrd.open_workbook("file.xls")
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
###  Set default index
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
### Iterate over sheet rows and show specific row and column
print(sh.cell_value(rowx=29, colx=5))

### Show every row on sheet
#for row_id in range(sh.nrows):
#    print(sh.row(row_id))

### Open CSV file and content of excel write to csv
with open("file.csv", 'w') as file:
    writer = csv.writer(file, delimiter = ",")
    header = [cell.value for cell in sh.row(0)]
    print(header)
    writer.writerow(header)

    for row_id in range(sh.nrows):
        row = [int(cell.value) if isinstance(cell.value, float) else cell.value for cell in sh.row(row_id)]
        writer.writerow(row)