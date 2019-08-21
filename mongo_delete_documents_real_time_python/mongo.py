from datetime import datetime, timedelta
import pymongo

## REASON, I need to connect mongo db and delete some days before file in the realtime

# CONNECTION SIDE
def get_test_db():
    client = pymongo.MongoClient('192.168.1.1:27017')
    db = client.requestLogs
    return db

#RENAME COLLECTION for the new datas write new documents
get_test_db()["requestLog"].rename("requestLog_bck")


# Take 5 day data from renamed collection(requestLog_bck) and insert new collection(requestLog)
N = 5
date_N_days_ago = datetime.now() - timedelta(days=N)
date_N_days_ago = date_N_days_ago.strftime("%Y%m%d%H%M%S%f")

aggregation_string = [{"$match": {'startTime': {"$gte": date_N_days_ago}}}, {"$out": "requestLog"}]
get_test_db().requestLog_bck.aggregate(aggregation_string)

# DROP renamed collection
get_test_db().requestLog_bck.drop()

