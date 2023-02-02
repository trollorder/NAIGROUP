import sqlite3
import time
'''
Motive: to convert realtime count data into instructions of the following 

'Red'
'Orange'
'Green'

For respective LED triggers

'''

class LEDinstructor():
    def __init__(self,dbconnectionpath:str,lednumber) -> None:
        self.dbconnection = sqlite3.connect(dbconnectionpath)
        self.cursor = self.dbconnection.cursor()
        self.lednumber = lednumber
        
    def getlatestentry(self):
        command = 'SELECT * FROM counttable ORDER BY datetime DESC LIMIT 1;'
        self.cursor.execute(command)
        return self.cursor.fetchone()#returns in tuple per column
    def processinstruction(self):
        thresholdtable = {'Red':20,'Orange':15,'Green':10}
        rowentry = self.getlatestentry()
        print(rowentry)
        instruction = 'Red'
        for colour in thresholdtable.keys():
            if int(rowentry[self.lednumber+1]) <= thresholdtable[colour]:
                instruction = colour
            else:
                pass
        #get instructions
        return instruction
    
newled = LEDinstructor('count.db',1)
while True:
    print(newled.processinstruction())
    time.sleep(1) #1 second sample rate
