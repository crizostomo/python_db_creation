import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

sql = "UPDATE employee SET address='San Andreas, 4000 - California' WHERE name='Diogo'"
mycursor.execute(sql)

mydb.commit()