from datetime import datetime, timedelta
import time
b_date = "20180929105245631"
a_date =  "20180829105245631"
a_date1 = "20180829"
a_date2 = "20180929"
datetime_object_b = datetime.strptime(b_date, "%Y%m%d%H%M%S%f")
datetime_object_a = datetime.strptime(a_date, "%Y%m%d%H%M%S%f")
datetime_object1 = datetime.strptime(a_date1, "%Y%m%d")
datetime_object2 = datetime.strptime(a_date2, "%Y%m%d")
print(datetime_object_a)
print(datetime_object_b)
print(datetime_object1)
print(datetime_object2)

if datetime_object_a < datetime_object_b:
    print ("SalamM")

if datetime_object1 < datetime_object2:
    print("Salam")
else:
    print("S")

N = 90
date_N_days_ago = datetime.now() - timedelta(days=N)
print(datetime.now())
print(date_N_days_ago)


if date_N_days_ago > datetime_object_b:
    print("Kicikdir")
"""
now = datetime.datetime.now()
print("Current date and time using str method of datetime object:")
print(str(now))
print "Current date and time using instance attributes:"
print "Current year: %d" % now.year
print "Current month: %d" % now.month
print "Current day: %d" % now.day
print "Current hour: %d" % now.hour
print "Current minute: %d" % now.minute
print "Current second: %d" % now.second
print "Current microsecond: %d" % now.microsecond

new_date = str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second)
print(new_date)

"""

print('-----------------')
a = datetime.now()
time.sleep(5)
b = datetime.now()
print(b-a)