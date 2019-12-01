import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="spectrum"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM contact")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
