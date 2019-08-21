import time
import datetime
# s = "01/12/2011"
s = "2018-08-31 12:03:16"
epoch = time.mktime(datetime.datetime.strptime(s, "%Y-%m-%d %H:%M:%S").timetuple())

print(epoch)

s1 = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
print(s1)



epoch_updateon.append(time.mktime(datetime.datetime.strptime(str(row[10]), "%Y-%m-%d %H:%M:%S").timetuple()))