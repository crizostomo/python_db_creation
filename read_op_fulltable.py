import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()
mycursor.execute("Select * from employee")

myresult = mycursor.fetchall()

for row in myresult:
    print(row)
