import threading
import time, sqlite3


class myThread(threading.Thread):

   def __init__(self, pn, icm):
       threading.Thread.__init__(self)
       self.pn = pn
       self.icm = icm

       self.con = sqlite3.connect("DB.db", check_same_thread=False)
       self.cursor = self.con.cursor()
       self.cursor.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY AUTOINCREMENT, pn VARCHAR(100), icm VARCHAR(100))")



   def run(self):

       self.cursor.execute("INSERT INTO test VALUES(NULL, '"+self.pn+"', '"+self.icm+"')")
       self.con.commit()
       self.con.close()



for i in range(0, 300):

    myThread("ABCDEFG", "12345678").start()