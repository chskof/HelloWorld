import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="chstest"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM person")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
