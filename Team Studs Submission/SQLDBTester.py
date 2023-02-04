import sqlite3
from random import randint
import datetime
import time
class datainserter():

   def __init__(self, stationdbpath:str,traindbpath:str) -> None:
      # try to establish connection to database,
      # will create DB_FILE if it does not exist
      self.stationcursor = sqlite3.connect(stationdbpath)
      self.traincursor=sqlite3.connect(traindbpath)

   def update_dbwithfalsevalues(self) -> None:
      """Helper function to save current time stamp, hand direction and
      wave count into DB wavetable.
      """
      now = datetime.datetime.now()
      dt_str = f"{now:%Y-%m-%d %H:%M:%S}"
      sql = """ INSERT INTO stationcounttable(datetime,uniqueperson,stationcount)
                values (?,?,?) """
      self.stationcursor.execute(sql, (dt_str, "Artifical Data", randint(1,20)))
      self.stationcursor.commit()
      sql2 = """ INSERT INTO traincounttable(datetime,uniqueperson,traincount)
                values (?,?,?) """
      self.traincursor.execute(sql2, (dt_str, "Artifical Data", randint(1,20)))
      self.traincursor.commit()
      
newdbupdator = datainserter("stationcount.db","traincount.db")

for x in range(1000):
   time.sleep(1)
   print("Updated")
   newdbupdator.update_dbwithfalsevalues()
