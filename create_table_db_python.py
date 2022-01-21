import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

mycursor.execute("Create table employee (name varchar(200), sal int(20))")