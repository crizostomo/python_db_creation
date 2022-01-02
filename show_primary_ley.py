import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

mycursor = mydb.cursor()

    # SQL Show statement to get primary key
sqlStatement = "SHOW keys FROM employee WHERE Key_name='PRIMARY'"

    # Execute the SHOW keys statement
mycursor.execute(sqlStatement)

    # Fetch all the rows


myresult = mycursor.fetchall()

for row in myresult:
    print(row)
