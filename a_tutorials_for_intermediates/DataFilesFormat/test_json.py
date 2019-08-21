import pandas as pd

print(pd.read_csv('schedule.csv'))

data=pd.read_csv('schedule.csv')
data.loc[[1, 3], ['title', 'rating']]

#Convert CSV to JSON
print(data.to_json(orient='records',lines=True))
