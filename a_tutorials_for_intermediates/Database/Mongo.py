from datetime import datetime, timedelta
import time

# Connection side
def get_db():
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client.myFirstMB
    return db


#def add_country(db):
#    db.countries.insert({"Name": "Canada"})

#def get_country(db):
#    return db.countries.find_one()
#if __name__ == "__main__":
#    db = get_db()
#    add_country(db)
#    print(get_country(db))



myrecord = {"author": "Duke", "title" : "PyMongo 101", "tags" : ["MongoDB", "PyMongo", "Tutorial"], "date" : datetime.datetime.utcnow()}
myrecord2 = [
        { "author": "Duke II",
          "title" : "PyMongo II 101",
          "tags" : ["MongoDB II", "PyMongo II", "Tutorial II"],
          "date" : datetime.datetime.utcnow() },
        { "author": "Duke III",
          "title" : "PyMongo III 101",
          "tags" : ["MongoDB III", "PyMongo III", "Tutorial III"],
          "date" : datetime.datetime.utcnow() }
        ]

myrecord3 = [{"author": "Duke 4",
              "title" : "PyMongo 101-A6",
              "tags" : ["MongoDB 6", "PyMongo 6", "Tutorial 6"],
              "date" : "20180929104903658"},
             {"author": "Adja",
              "title": "MongoDB 101-A7",
              "note": "Schema free MongoDB",
              "date": "20180829104856817"},
              {
               "author": "Duke 5",
               "title" : "PyMongo 101 - 5",
               "tags" : ["MongoDB 5", "PyMongo 101 - A5", "Tutorial 5"],
               "date" : "20180729104856817"
               },
                {
               "author": "Duke 6",
               "title" : "PyMongo 105 - 5",
               "tags" : ["MongoDB 6", "PyMongo 101 - A5", "Tutorial 5"],
               "date" : "20180629104856817"
               },
                {
               "author": "Duke 7",
               "title" : "PyMongo 106 - 5",
               "tags" : ["MongoDB 7", "PyMongo 101 - A5", "Tutorial 5"],
               "date" : "20180529104856817"
             }]


# record_id = get_db().title.insert(myrecord)
# record_id = get_db().title.insert(myrecord2)
record_id = get_db().author.insert(myrecord3)
#print(record_id)
#print(get_db().collection_names())

for post in get_db().author.find():
    print(post)

import pymongo
def get_db_localhost():
    import pymongo
    client = pymongo.MongoClient('localhost:27017')
    db = client.myFirstMB
    return db


get_db_localhost().titleagfr.createIndex([("date", pymongo.ASCENDING), ("author", pymongo.DESCENDING)], background=True)

help(get_db_localhost().titleagfr.createIndex)
myrecord3 = [{"author": "Duke 4",
              "title": "PyMongo 101-A6",
              "tags": ["MongoDB 6", "PyMongo 6", "Tutorial 6"],
              "date": "20180929104903658"},
             {"author": "Adja",
              "title": "MongoDB 101-A7",
              "note": "Schema free MongoDB",
              "date": "20180829104856817"},
              {
               "author": "Duke 5",
               "title": "PyMongo 101 - 5",
               "tags": ["MongoDB 5", "PyMongo 101 - A5", "Tutorial 5"],
               "date": "20180729104856817"
               },
                {
               "author": "Duke 6",
               "title": "PyMongo 105 - 5",
               "tags": ["MongoDB 6", "PyMongo 101 - A5", "Tutorial 5"],
               "date": "20180629104856817"
               },
                {
               "author": "Duke 7",
               "title": "PyMongo 106 - 5",
               "tags": ["MongoDB 7", "PyMongo 101 - A5", "Tutorial 5"],
               "date": "20180529104856817"
             },
             {
               "author": "Duke 7",
               "title": "PyMongo 106 - 5",
               "tags": ["MongoDB 7", "PyMongo 101 - A5", "Tutorial 5"],
               "date": "20180429104856817"
             }
             ]

#INSERT DATA
#get_db_localhost().title.insert(myrecord3)

#  RENAME COLLECTION Rename(new_name, session=None, **kwargs)
#get_db_localhost()["author_test1"].rename("author")

N = 120
date_N_days_ago = datetime.now() - timedelta(days=N)
date_N_days_ago = date_N_days_ago.strftime("%Y%m%d%H%M%S%f")
#get_db_localhost().title.find({'date': {"$gte": "20180729104856817"}}).forEach(function(doc){get_db_localhost().title3.insert(doc)});           # work very slow
#get_db_localhost().title2.aggregate([ { $match: {'date': {"$gte": "20180729104856817"}} }, { $out: "titleagfr1" } ])                                      # works very fastly

#aggregation_string = [{"$match": {'date': {"$gte": "20180729104856817"}}}, {"$out": "titlesalam"}]
#get_db_localhost().title2.aggregate(aggregation_string)





# Check All data
#for post in get_eqaime_db().requestLog.find():
#    print(post)

#for post in get_eqaime_db().requestLog.find({"requestNumber": "1U5T3J5N572Y5"}):
#for post in get_eqaime_db().requestLog.find():
#    print(post)

#Count of the matching number
#print(get_eqaime_db().requestLog.find({"requestNumber": "1U5T3J5N572Y5"}).count())
#print(datetime.datetime.utcnow)
#for post in get_eqaime_db().requestLog.find({"time": {"$lte": isodate("20180829105245947")}}):
 #   print(post)
