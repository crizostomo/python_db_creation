import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root")

if(mydb):
    print("Connection Successful")
else:
    print("Connection Unsuccessful")

mycursor = mydb.cursor()
mycursor.execute("Create database staff")