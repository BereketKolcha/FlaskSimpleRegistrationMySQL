import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  username="root",
  password="",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
#-----------------------------create table-------------------------------------------------
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#-----------------------------insert-------------------------------------------------------
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")
#-------------------------------select-------------------------------------------------------
mycursor.execute("SELECT * FROM customers where name = 'John'")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)