import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

query="ALTER TABLE employee ADD Profession VARCHAR(100)"
mycursor.execute(query)
mydb.commit()
print("NEW COLUMN ADDED..")