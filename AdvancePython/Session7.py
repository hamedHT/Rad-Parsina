import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="837883",
  database="mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

#--------------------------------------------------------------------------------

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#_____________________________________________________________________________________

sql = "UPDATE customers SET address = 'Canyon 123' WHERE name = 'john'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

#________________________________________________________________________________________

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")