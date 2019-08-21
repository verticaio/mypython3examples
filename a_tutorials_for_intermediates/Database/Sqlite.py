from sqlalchemy import create_engine
from pandas.io import sql
import pandas


data = pandas.read_csv('schedule.csv', encoding="ISO-8859-1")
engine = create_engine('sqlite:///:memory:')   #Create db engine on memory
# engine = create_engine('sqlite:////home/babak/PycharmProjects/OOP/Database/test.db')  #Create db engine on file
data.to_sql('data_table', engine)    #Store dataframe as table

print(pandas.read_sql_query('SELECT * FROM data_table', engine))

#Insert
sql.execute('INSERT INTO data_table VALUES(?, ?, ?, ?, ?, ?)', engine, params=[(5, 6, 'Austindasda', '19:30-20:00', 'Comdasdedy', 6.0)])
print(pandas.read_sql_query('SELECT * FROM data_table', engine))

#Delete
sql.execute('DELETE FROM data_table where rating=6.0', engine)
print(pandas.read_sql_query('SELECT * FROM data_table', engine))