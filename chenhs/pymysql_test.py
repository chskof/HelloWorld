import pymysql

db = pymysql.connect("localhost","root","123456","chstest" )
cursor = db.cursor()
cursor.execute("SELECT name from person where id='1'")
data = cursor.fetchone()
print(str(data))
