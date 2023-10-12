from flask import Flask
import serial

app = Flask(__name__)

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # for linux
ser = serial.Serial('COM3', 9600, timeout=1) # for windows 
# mode | find "COM" # use this command to find the serial port in terminal

temperature = ser.readline().decode()
temperature = temperature.rstrip("\r\n")

@app.route("/")
def hello_world():
    return "<p>temperature : {}</p>".format(temperature)