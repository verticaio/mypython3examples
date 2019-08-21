import sys, os
import pymysql as mdb
import csv


# Read CSV file and  export host ip
os.chdir("/home/babak/PycharmProjects/OOP/DataFilesFormat/")
rows = []
ip_excel_rows = []
with open('2018gen.csv', 'r+') as file:
    reader = csv.reader(file)  # Read Object
    for row in reader:
        if "." in str(row[2]):
            rows.append(row)
for i in rows:
    ip_excel_rows.append(i[2])




class MyDbCon:
    def __init__(self, host, user, passw, db):
        try:
            self.con = mdb.connect(host, user, passw, db)
            self.cur = self.con.cursor()
        except:
            print("DB connection error happened")
            sys.exit(1)
    def zab_comp_db(self):
        try:
            ip_zabbix_rows = []
            notindb_rows = []
            notinexcel_rows = []
            shared_rows = []
            select_query = 'select ip from zabbixdb.interface'
            self.cur.execute(select_query)
            ip_list = list(self.cur.fetchall())
            for b in ip_excel_rows:
                for record in ip_list:
                    a = record[0]
                    if b != a:
                        notindb_rows.append(b)
                        notinexcel_rows.append(a)
                    else:
                        shared_rows.append(a)
            print("Excelde olub zabbix databasinde olmayan IPler:", list(set(notindb_rows)))
            print("Zabbix db de olub excelde olmayan:",  list(set(notinexcel_rows)))
            print("Eyni IPler:", shared_rows)
        except:
            print("Sorry, we encountered a problem")

if __name__ == '__main__':
    db = MyDbCon('1192.168.1.1', 'username', 'pass', 'zabbixdb')
    print(db.zab_comp_db())







