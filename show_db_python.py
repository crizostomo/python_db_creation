import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root")

mycursor = mydb.cursor()

mycursor.execute("Show databases")

for db in mycursor:
    print(db)

#1º Rota = Cadastrar = Similar ao flask, vc vai preencher seu nome e idade e ao preencher vai inputar no meu banco de dados
#2º Rota = Consultar os dados que foram inputados