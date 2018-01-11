from Database import Database
from flask import Flask, jsonify
class ProgrammingDone:

    def getAll(self):
        database = Database()
        databaseConn = database.databaseConnection()
        query = "SELECT * FROM `programmin_done`"
        curA = databaseConn.cursor(buffered=True)
        curA.execute(query)
        dataReturned = curA.fetchall()
        print (dataReturned)

        for (id, test, en, en) in curA:
            print(str(id) + ' ' + str(test))
        databaseConn.close()

    #def getEntryForUser(self):

    #def changeValues(self):


ProgrammingDone.getAll(ProgrammingDone)
