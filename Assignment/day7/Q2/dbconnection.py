import mysql.connector


def getconnection():
    connection = mysql.connector.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "root",
        database = "iot_dataagriculture",
        use_pure = True
    )

    return connection