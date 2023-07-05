import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="testdb"
)
# print(db)
mycursor=db.cursor()
# mycursor.execute("create table student (id primary key, name varchar(20), city varchar(20)")
mycursor.execute("insert into student values(%s,%s,%s)")
val=(1,"kiran","nashik")
db.commit()
print(mycursor.rowcount,"row added")
