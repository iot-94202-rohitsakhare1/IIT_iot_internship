from flask import Flask, request

server = Flask(__name__)

@server.get('/')
def home():
    return "Server is running"

@server.post('/temperature<temp>')
def add_temperature(temp):

    file = open("temperature.txt", "a")
    file.write(temp + "\n")
    file.close()

    return "Temperature added: " + temp

@server.put('/temperature<temp>')
def update_temperature(temp):

    file = open("temperature.txt", "w")
    file.write(temp + "\n")
    file.close()

    return "Temperature updated to: " + temp


@server.get('/temperature')
def get_temperature():
    file = open("temperature.txt", "r")
    data = file.read()
    file.close()

    return "Temperature Readings" + data 

@server.post('/light<light>')
def add_light(light):

    file = open("light.txt", "a")
    file.write(light + "\n")
    file.close()

    return "Light intensity added: " + light


@server.put('/light<light>')
def update_light(light):

    file = open("light.txt", "w")
    file.write(light + "\n")
    file.close()

    return "Light intensity updated to: " + light

@server.get('/light')
def get_light():
    file = open("light.txt", "r")
    data = file.read()
    file.close()

    return "Light Intensity Readings = " + data 


server.run(host='0.0.0.0',port=4000, debug=True)