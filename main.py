import serial
import matplotlib.pyplot as plt
from matplotlib import animation
import time

# ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) # for linux
ser = serial.Serial('COM3', 9600, timeout=1) # for windows 
# mode | find "COM" # use this command to find the serial port in terminal

max_size = 50
data = []

# define figure
fig = plt.figure()

while True:
    try:
        # serial
        temperature = ser.readline().decode()
        temperature = temperature.rstrip("\r\n")
        # print(data.decode())

        if len(data) >= max_size:
            data.pop(0)
        data.append(float(temperature))
        # print("----------")
        print(temperature)
        time.sleep(1) # seconds

        # figure
        # plt.plot(data)
        # plt.draw()
        # plt.pause(1)
        # plt.cla()
    #     if len(data) >= max_size:
    #         break
    # plt.plot(data)
    # plt.ylim(-10,40)
    # plt.savefig("./figure/fig.png")

    except KeyboardInterrupt as e:
        print("Keyboard Interupt")
        break
ser.close()