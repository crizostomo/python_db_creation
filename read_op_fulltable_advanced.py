import mysql.connector

try:
    mydb = mysql.connector.connect(host="localhost", user="root", database="staff")

    sql_select_Query = "Select * from employee"
    mycursor = mydb.cursor()
    mycursor.execute(sql_select_Query)
    # get all records
    records = mycursor.fetchall()
    print("Total number of rows in table: ", mycursor.rowcount)

    print("\nPrinting each row\n")
    for row in records:
        print("name = ", row[0])
        print("sal  = ", row[1])
        print("Address  = ", row[2])
        print("Profession  = ", row[3], "\n")


except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if mydb.is_connected():
        mydb.close()
        mydb.close()
        print("MySQL connection is closed")
