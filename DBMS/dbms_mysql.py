import pymysql
conn = pymysql.connect(
    host ="localhost",
    user = "root",
    password ="1234",
    database="exampledb",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()
cursor.execute("SELECT DATABASE()")
print("현재 데이터베이스:",cursor.fetchone())
conn.close()