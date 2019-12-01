import pymysql

db = pymysql.connect("localhost","root","123456","spectrum" )
cursor = db.cursor()
cursor.execute("SELECT name from contact where id='1'")
data = cursor.fetchone()
print(str(data))
