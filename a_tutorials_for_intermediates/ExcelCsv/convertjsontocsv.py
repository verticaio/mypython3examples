import csv, json, sys
#if you are not using utf-8 files, remove the next line
sys.setdefaultencoding("UTF-8") #set the encode to utf8
#check if you pass the input file and output file
if sys.argv[1] is not None and sys.argv[2] is not None:
    fileInput = sys.argv[1]
    fileOutput = sys.argv[2]
    inputFile = open(fileInput) #open json file
    outputFile = open(fileOutput, 'w') #load csv file
    data = json.load(inputFile) #load json content
    inputFile.close() #close the input file
    output = csv.writer(outputFile) #create a csv.write
    output.writerow(data[0].keys())  # header row
    for row in data:
        output.writerow(row.values()) #values row

# python json_to_csv.py input.txt output.csv

# Second example.
#http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/

## Import json to elastic search
#https://medium.com/@shaonshaonty/export-data-from-elasticsearch-to-csv-caaef3a19b69
#http://carrefax.com/new-blog/2018/3/12/load-json-files-into-elasticsearch
# Export  as csv from elasticsearch json 
#https://qbox.io/blog/how-to-export-data-elasticsearch-into-csv-file