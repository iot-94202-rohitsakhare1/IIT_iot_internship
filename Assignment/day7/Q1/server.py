from flask import Flask, request
from executeQuery import executeQuery
from executeselectQuery import executeSelectQuery
from datetime import datetime

server = Flask(__name__)

@server.get('/')
def homepage():
    return "Welcome. This is home page."

@server.post('/iot')
def create_data():
    id = request.form.get("id")
    temperature = request.form.get("temperature")
    humidity = request.form.get("humidity")

    query = """
    INSERT INTO sensor_readings (id, temperature, humidity, created_at)
    VALUES (%s, %s, %s, %s)
    """
    values = (id, temperature, humidity, datetime.now())
    executeQuery(query, values)

    return "Data added successfully"

@server.put('/iot')
def update_data():
    id = request.form.get('id')
    temperature = request.form.get('temperature')

    query = "UPDATE sensor_readings SET temperature=%s WHERE id=%s"
    values = (temperature, id)
    executeQuery(query, values)

    return "Temperature updated successfully"

@server.get('/iot')
def get_data():
    query = "SELECT * FROM sensor_readings"
    data = executeSelectQuery(query)
    return str(data)

@server.delete('/iot')
def delete_data():
    id = request.form.get('id')
    query = "DELETE FROM sensor_readings WHERE id=%s"
    executeQuery(query, (id,))
    return "Data deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
