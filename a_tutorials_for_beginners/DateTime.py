# Date and time objects : Naive and aware
import datetime
import time
print "Max Year:", datetime.MAXYEAR
print "Mix Year:", datetime.MINYEAR

d = datetime.date(2018,07,04)
print d

today = datetime.date.today()
print(today)

print time.time()
print(datetime.date.fromtimestamp(time.time()+999999))

print(datetime.date.min)
print(datetime.date.max)
print(datetime.date.resolution)


print d.year,d.month

print "Before:", d
d=d.replace(month=12,day=30)
print "Then:  ", d

print "Show detailed info about d: ", d.timetuple()
print d.weekday()
print d.isoweekday()
print d.isocalendar()
print d.isoformat()

print("-------------------------------------------")
print d.__str__()
print d.ctime()

print "-----------------------------------------"
d_new = datetime.date(2018,07,04)
td = datetime.timedelta(0,99999)
d1=d_new+td
print d1


print d1>d_new