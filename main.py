import serial
import matplotlib.pyplot as plt
from matplotlib import animation

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

max_size = 50
data = []

# define figure
fig = plt.figure()

while True:
    # serial
    temperature = ser.readline().decode()
    temperature = temperature.rstrip("\r\n")
    # print(data.decode())

    if len(data) >= max_size:
        data.pop(0)
    data.append(float(temperature))
    # print("----------")
    # print(data)

    # figure
    # plt.plot(data)
    # plt.draw()
    # plt.pause(1)
    # plt.cla()
    if len(data) >= max_size:
        break
plt.plot(data)
plt.ylim(-10,40)
plt.savefig("./figure/fig.png")
ser.close()