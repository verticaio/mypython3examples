import pymysql
import json
import collections
import requests
import os

## REASON, I want to know when any ticket assign to me. For this I have to check new tickets in redmine db in every minute. After find new ticket send  to hook 

# redmine db connection side
db = pymysql.connect("192.168.1.1", "redmine", "redmine", "redminedb", use_unicode=True, charset='utf8')
cursor = db.cursor()

# 53 is my id on the redmine db

# Honestly i didn't send any attachmet from redmine db to my hook.

check_file = os.stat("updateon.txt").st_size
if check_file > 0:
    a = open('updateon.txt', 'r+')
    updateon1 = a.read()
else:
    updateon1 = '2000-01-01 00:00:00'
select_query = "SELECT issues.id, " \
               " projects.NAME, " \
               "trackers.NAME AS TRACKER, " \
               " issues.SUBJECT,  " \
               "issues.description, " \
               "issues.due_date, " \
               "issues.estimated_hours," \
               " issue_statuses.name AS STATUS, " \
               "issues.priority_id, " \
               "CONCAT( users.firstname, ' ', users.lastname ) AS AUTHOR, " \
               "issues.created_on, " \
               "issues.updated_on, " \
               "issues.done_ratio, " \
               "parent_issues.SUBJECT AS parent " \
               "FROM issues " \
               "LEFT JOIN projects ON issues.project_id = projects.ID " \
               "LEFT JOIN trackers ON issues.tracker_id = trackers.ID  " \
               "LEFT JOIN issue_statuses ON issues.status_id = issue_statuses.ID " \
               "LEFT JOIN users ON issues.author_id = users.ID " \
               "LEFT JOIN issues AS parent_issues ON issues.parent_id = parent_issues.ID " \
               "WHERE " \
               "(( issues.assigned_to_id = 53 ) OR ( issues.id IN ( SELECT DISTINCT watchers.watchable_id FROM watchers " \
               "WHERE watchers.user_id = 53 ) )) AND issues.status_id NOT IN ( 5, 6 ) AND issues.updated_on > " \
               " '"+updateon1+"' ORDER BY issues.updated_on DESC ;"



cursor.execute(select_query)
rows = cursor.fetchall()
epoch_updateon = []
rowarray_list = list(rows)
objects_list = []

# Eger Rowarray_list ishinde hecne yoxdursa onda programdan cixsin, bu o demekdir ki update vaxtindan beri ish acilmayib
if len(rowarray_list) <= 0:
    exit()

# Liste yigdigim datani key value seklinde collectionlara yigiram
for row in rowarray_list:
    d = collections.OrderedDict()
    d['issues.id'] = row[0]
    d['projects.name'] = row[1]
    d['trackers.name'] = row[2]
    d['issues.subject'] = row[3]
    d['issues.description'] = row[4]
    d['issues.due_date'] = str(row[5])
    d['issues.estimated_hours'] = row[6]
    d['issue_statuses.name'] = row[7]
    d['issues.priority_id'] = row[8]
    d['author'] = row[9]
    d['issues.created_on'] = str(row[10])
    d['issues.updated_on'] = str(row[11])
    d['issues.done_ratio'] = row[12]
    d['parent'] = row[12]
    epoch_updateon.append(str(row[11]))
    objects_list.append(d)

# Fayl
with open('updateon.txt', 'w') as f:
    f.write(str(epoch_updateon[0]))

j = json.dumps(objects_list)
objects_file = 'student_objects.js'
f = open(objects_file, 'w')
for person in j:
    f.write(person)
API_ENDPOINT = "https://hook.io/babakli/red_mine"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
r = requests.post(url=API_ENDPOINT, data=json.dumps(objects_list), headers=headers)
print(r.status_code)
print(r.json())

db.close()
