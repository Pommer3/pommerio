from Database import Database
import json


class ProgrammingDone:

    def getAll(self):
        database = Database()
        databaseConn = database.databaseConnection()
        query = "SELECT * FROM `programmin_done`"
        cur = databaseConn.cursor(buffered=True)
        cur.execute(query)
        data = [dict((cur.description[i][0], value)
                     for i, value in enumerate(row)) for row in cur.fetchall()]

        for entry in data:
            entry["last_entry"] = str(entry.get("last_entry"))

        jsonOut = json.dumps(data)
        print(jsonOut)
        databaseConn.close()

    def incrementProgrammingHour(self, userID):
        database = Database()
        conn = database.databaseConnection()
        query = "UPDATE `programmin_done`SET `hours_so_far`= 1 + (SELECT `hours_so_far` FROM (SELECT * FROM " \
                "`programmin_" \
                "done` WHERE user_id = 1) AS Copy) WHERE `user_id`=" + str(userID)
        cur = conn.cursor(buffered=True)
        cur.execute(query)
        conn.commit()
        conn.close()
        data = {'success': True}
        return json.dumps(data)


