import pandas as pd

data = pd.read_csv('schedule.csv')
#Read All FILE

print(data)
#Read some rows
print(data[0:3])

#Read Column
print(data.loc[:, ['title']])

#Reading certain rows and certain columns, 0,1,3 pythonun ozunun sira

print(data.loc[[0, 1, 3], ['id', 'title', 'rating']])


#Reading certain columns for a range of rows
print(data.loc[1:3, ['id', 'title', 'rating']])

fields = []

