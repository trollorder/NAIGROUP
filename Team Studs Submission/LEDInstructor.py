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
    def __init__(self,stationdb:str,traindb:str,lednumber) -> None:
        self.stationdbconnection = sqlite3.connect(stationdb)
        self.stationcursor = self.stationdbconnection.cursor()
        self.traindbconnection = sqlite3.connect(traindb)
        self.traincursor = self.traindbconnection.cursor()
        self.lednumber = lednumber
        
    def getlatestentry(self):
        stationcommand = 'SELECT * FROM stationcounttable ORDER BY datetime DESC LIMIT 1;'
        traincommand = 'SELECT * FROM traincounttable ORDER BY datetime DESC LIMIT 1;'
        self.stationcursor.execute(stationcommand)
        self.traincursor.execute(traincommand)
        return self.stationcursor.fetchone(),self.traincursor.fetchone()#returns in tuple(tuple()) per column
    def processinstruction(self):
        thresholdtable = {'Red':35,'Orange':34,'Green':17}
        stationdata,traindata= self.getlatestentry()
        stationcount=stationdata[self.lednumber+1]
        traincount = traindata[self.lednumber+1]
        totalcount = int(traincount) + int(stationcount)
        print("Station Count is {}, Train Count is {}, Total Count is{}.".format(stationcount,traincount,totalcount))
        instruction="Red"
        for colour in thresholdtable.keys():
            if totalcount <= thresholdtable[colour]:
                instruction = colour
            else:
                pass
        #get instructions
        return instruction

    

