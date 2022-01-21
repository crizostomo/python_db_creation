import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

#https://pynative.com/python-mysql-database-connection/

mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE employee CHANGE name Name varchar(200)")