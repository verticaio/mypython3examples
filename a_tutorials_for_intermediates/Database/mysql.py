import pymysql

#db_connect = pymsql.connect("host", "user", "pass", "db_name")
db = pymysql.connect("localhost", "python", "python", "demo")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
print("You're running version", cursor.fetchone())

#Drop table
cursor.execute("DROP TABLE IF EXISTS student")


#Create Table
create_table_query = """CREATE TABLE student(fname VARCHAR(20), lname VARCHAR(20),
age INT, enrolment_no VARCHAR(12))"""
cursor.execute(create_table_query)

#Show Table Comun Information. sene printi olan queryi ishledirsen sonr onu fetchone edirsne
cursor.execute("DESCRIBE student;")
print(cursor.fetchone())

cursor.execute("SHOW COLUMNS FROM student;")
print(cursor.fetchone())

# Insert Into to Mysql
insert_query = 'INSERT INTO student VALUES("Gulehmed","Mammadli",22,"0812CS141028")'
insert_query_2 = 'INSERT INTO student VALUES("Gulehmed12","Cavadov",25,"0812CS141908")'
insert_query_3 = 'INSERT INTO student VALUES("Babak","Sharifov",33,"9992CS141908")'
try:
    cursor.execute(insert_query)
    cursor.execute(insert_query_2)
    cursor.execute(insert_query_3)
    db.commit()   #Commit writing to the database
except:
    db.rollback()  # Rollback the transaction if not complete
    print("Problem with inserting to table")

def select():
#Select query
    select_query = 'SELECT * from student;'
    cursor.execute(select_query)

#print(cursor.fetchone())     # bu ise obsi setin ichinden birinci secir
#print(cursor.fetchall())  # bu butun seti cekir ve dailindeki her bir set bir row olur
#Asagidaki formada bir her bir datani tek formada cixartiq yoxsa set seklinde data qaydir from mysql

    try:
        cursor.execute(select_query)
        resultset = cursor.fetchall()   #To fetch all records that satisfy
        for record in resultset:
            fname = record[0]
            lname = record[1]
            age = record[2]
            enrolment_no = record[3]
            print("Student: {0} {1}; Enrolment: {2}; Age: {3}".format(fname, lname, enrolment_no, age))
    except:
        print("Sorry, we encountered a problem")


select()

#UPDATE procedur

update_query = 'update student set age=age+1 where age<=25'

try:
    cursor.execute(update_query)
    db.commit()
    print("After Update: \n ")
    select()
except:
    db.rollback()

# Delete Records
delete_query = "delete from student where age>26"
try:
    cursor.execute(delete_query)
    db.commit()
    print("After Delete: \n")
    select()
except:
    db.rollback()



#Closing the database connection
db.close()


"""
Links for mysql class 
https://github.com/nestordeharo/mysql-python-class
https://codereview.stackexchange.com/questions/39009/python-connection-with-mysql
https://softwareengineering.stackexchange.com/questions/261933/using-one-database-connection-across-multiple-functions-in-python
"""