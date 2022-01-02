import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

sqlform = "Insert into employee(name,sal) values(%s,%s)"

employees = [("Janaina", 55000), ("Ana", 18000), ("Joao", 32000), ]

mycursor.executemany(sqlform, employees)

mydb.commit()