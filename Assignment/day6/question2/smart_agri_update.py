import mysql.connector
connection=mysql.connector.connect(
host="127.0.0.1",
port="3306",
user ="root",
password="root",
database="mysqldb",
use_pure=True
)

sensor_id=input("enter sensor_id whose moisture_level tobe change")
moisture_level=input("enter new moisture_level")

query=f"update smart_agri SET moisture_level='{moisture_level}' WHERE sensor_id='{sensor_id}';"

cursor=connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()