from datetime import datetime, timedelta
import time
from pymongo import MongoClient
from pprint import pprint
import pymysql
import uuid
import shlex
from bson.objectid import ObjectId

# Login cedveli umumi login melumatini saxlayir.
# Contact cedveli kontact informasiyaini saxlayir(name, oz id si ve foreign keyle birinci login cedveline baglidir)
# Altcedveller ise contact cedveline baglidir.

## Mysql  DB connection config
mysql_db = pymysql.connect("localhost", "username", "pass", "dbname")
cursor = mysql_db.cursor()



## MongoDB  DB connection config
def get_mongo_db():
    client = MongoClient('localhost:27017')
    db = client.warehouse
    return db

# Create function for getting exist id because then if my code is stopped any reason and again I have to check exist id and insert other documents to rdbms
def get_exist_id():
    id_select_query = "select id from login"
    cursor.execute(id_select_query)
    records = cursor.fetchall()
    return records


db_list = list(get_exist_id())
mongo_db=get_mongo_db()
umongo_collection=mongo_db.umongo
i=0
##  Kod 5 for'dan ibaretdir. Birinci for general butun documentleri getirir ve bu documentleri bazaya insert edirik, login tablesine. 
for post in umongo_collection.find():
    i+=1
    if i%100==0:
        cursor.execute("select 1")
        print("Select 1 executed\n\n")
    id=str(post['_id'])
    login=str(post['login'])
    username=str(post['userName'])
    ## Check id exit on db , if exits dont insert 
    print(id)
    if id in str(db_list):
        continue
    print("Entered insert mode")
    login_query = "insert into login values('{}', '{}','{}')"
    cursor.execute(login_query.format(id,login,mysql_db.escape_string(username)).encode('utf-8'))
    for contact in post['contacts']:
        con_keys=list(contact.keys())
        contact_id=str(uuid.uuid4())
        for keys in con_keys:
            if keys=="name" or keys=="Name":
                name=str(contact[keys])
                contact_query = "insert into contacts values('{}', '{}','{}')"
                print("Inserted contacts table", id)
                cursor.execute(contact_query.format(contact_id,mysql_db.escape_string(name),id).encode('utf-8'))
        for keys in con_keys:
            if keys=="info" or keys=="Info":
                info=contact[keys]
                for info_k in info:
                    if info_k['k']=="Emails":
                        emails=info_k['v']
                        for email in emails:
                            email_id=str(uuid.uuid4())
                            email_v=email["v"]
                            email_k=email["k"]
                            email_query = "insert into Emails values('{}', '{}','{}','{}')"
                            print("Inserted Emails table", id)
                            cursor.execute(email_query.format(email_id,mysql_db.escape_string(email_v),mysql_db.escape_string(email_k),contact_id).encode('utf-8'))
                    if info_k['k']=="Numbers":
                        numbers=info_k['v']
                        for number in numbers:
                            number_id=str(uuid.uuid4())
                            num_v=number["v"]
                            num_k=number["k"]
                            number_query = "insert into Numbers values('{}', '{}','{}','{}')"
                            print("Inserted Numbers table", id)
                            cursor.execute(number_query.format(number_id,mysql_db.escape_string(num_v),mysql_db.escape_string(num_k),contact_id).encode('utf-8'))
                    if info_k['k']=="PersonalInfo":
                        personalinfo=info_k['v']
                        for personal in personalinfo:
                            personal_id=str(uuid.uuid4())
                            perinfo_v=personal["v"]
                            perinfo_k=personal["k"]
                            personal_query = "insert into PersonalInfo values('{}', '{}','{}','{}')"
                            print("Inserted PersonalInfo table", id)
                            cursor.execute(personal_query.format(personal_id,mysql_db.escape_string(perinfo_v),mysql_db.escape_string(perinfo_k),contact_id).encode('utf-8'))
                    if info_k['k']=="socialProfiles":
                        socialprofiles=info_k['v']
                        for social in socialprofiles:
                            social_id=str(uuid.uuid4())
                            soc_pro_v=social["v"]
                            soc_pro_k=social["k"]
                            social_query = "insert into SocialProfiles values('{}', '{}','{}','{}')"
                            print("Inserted socialprfiles table", id)
                            cursor.execute(social_query.format(social_id,mysql_db.escape_string(soc_pro_v),mysql_db.escape_string(soc_pro_k),contact_id).encode('utf-8'))

                    if info_k['k']=="Address":
                        address=info_k['v']
                        for addr in address:
                            addr_id=str(uuid.uuid4())
                            addr_v=addr["v"]
                            addr_k=addr["k"]
                            addr_query = "insert into Address values('{}', '{}','{}','{}')"
                            print(addr_query.format(addr_id,addr_v,addr_k,contact_id).encode('utf-8'))
                            cursor.execute(addr_query.format(addr_id,mysql_db.escape_string(addr_v),mysql_db.escape_string(addr_k),contact_id).encode('utf-8'))
    mysql_db.commit()
mysql_db.close()
