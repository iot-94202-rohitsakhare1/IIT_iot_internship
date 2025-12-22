# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host="127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "mysqldb",
    use_pure = True
)

# form a query to be executed in mysql
query = "select * from smart_agri";

# create cursor to execute query
cursor = connection.cursor()

# execute qeury with cursor
cursor.execute(query)

# get required data from cursor
smart_agri = cursor.fetchall()

for smart_agri in smart_agri:
    print(smart_agri)
    
# close the cursor
cursor.close()

# close connection with mysql server
connection.close()