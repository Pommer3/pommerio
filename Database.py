import mysql.connector

class Database:

    def __init__(self):
        # First we read in important access credentials that should not be shared with the world:
        accessFile = open("/var/www/html/credentials/credentials.txt", 'r')
        # Reading each line knowing the right order and stripping it for irritating newlines
        global username
        username = accessFile.readline().rstrip()
        global password
        password = accessFile.readline().rstrip()
        global database
        database = accessFile.readline().rstrip()
        global host
        host = accessFile.readline().rstrip()
    #Return a connection to the database
    def databaseConnection(self):

        cnx = mysql.connector.connect(user=str(username), password=str(password),
                                      host=host,
                                      database=str(database),
                                      use_pure=False)
        return cnx




