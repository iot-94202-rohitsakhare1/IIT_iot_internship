from flask import Flask, request, jsonify
from datetime import datetime
from executeQuery import executeQuery
from executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "Welcome. This is the IoT home page."

@server.post('/iot')
def create_data():
    sensor_id = request.form.get("sensor_id")
    humidity = request.form.get("humidity")
    query=f"insert into information values({sensor_id},{humidity},'{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}');"
    executeQuery(query)
    return "Data added successfully"

@server.put('/iot')
def update_data():
    sensor_id = request.form.get("sensor_id")
    humidity = request.form.get("humidity")
    query = f"UPDATE information SET moisture_lvl ={humidity } WHERE sensor_id={sensor_id};"
    executeQuery(query)
    return "Humidity updated successfully"

@server.get('/iot')
def get_data():
    query = "SELECT * FROM information;"
    data = executeSelectQuery(query)
    return str(data)

@server.delete('/iot')
def delete_data():
    sensor_id = request.form.get('sensor_id')
    query = f"DELETE FROM information WHERE sensor_id={sensor_id};"
    executeQuery(query)
    return "Data deleted successfully"

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
