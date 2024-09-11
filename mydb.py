import pymysql

dataBase = pymysql.connect(
    host='localhost',
    user='root',
    password='Qwaszx12@'
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE elderco")
print("All Done!")
