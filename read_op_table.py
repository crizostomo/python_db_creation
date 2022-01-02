import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()
mycursor.execute("Select name from employee")

myresult = mycursor.fetchone()

for row in myresult:
    print(row)