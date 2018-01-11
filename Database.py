import mysql.connector


#First we read in important access credentials that should not be shared with the world:

accessFile = open("credentials/credentials.txt", 'r')

#Reading each line knowing the right order and stripping it for irritating newlines
username = accessFile.readline().rstrip()
password = accessFile.readline().rstrip()
database = accessFile.readline().rstrip()

print(username+password+database)

cnx = mysql.connector.connect(user=str(username), password=str(password),
                              host='pommer.io',
                              database=str(database),
                              use_pure=False)

query ="SELECT * FROM `tester` WHERE 1"

curA = cnx.cursor(buffered=True)

curA.execute(query)

for (id, test) in curA:
    print(str(id) + ' ' + test)
cnx.close()
