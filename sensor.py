import gpiozero as gpio
from time import sleep



sensor = gpio.DistanceSensor(3,2)

while True:
    print('Distance: ',sensor.distance*100)
    sleep(1)