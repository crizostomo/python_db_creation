import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

sql = "DELETE FROM employee WHERE name='Pedro'"

mycursor.execute(sql)

mydb.commit()