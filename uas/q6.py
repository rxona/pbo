import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="dbName"
)

mycursor = mydb.cursor()

qry = "SELECT * FROM users"

print('Executing', qry)
mycursor.execute(qry)

result = mycursor.fetchall()

mydb.close()
