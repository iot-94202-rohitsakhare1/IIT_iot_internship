# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "mysqldb",
    use_pure = True
)

# form a query to be executed
sensor_id = int(input("Enter id : "))
moisture_level = input("Enter moisture level : ")
date_time = input("Enter timestamp : ")

query = f"insert into smart_agri values({sensor_id}, '{moisture_level}', '{date_time}');"

# create a cursor to execute a query
cursor = connection.cursor()

# execute a query
cursor.execute(query)

# commit your changes on mysql serer
connection.commit()

# close the cursor
cursor.close()

# close the connection with mysql server
connection.close()