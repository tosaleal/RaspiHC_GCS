import gpiozero as gpio
from time import sleep



sensor = gpio.DistanceSensor(trig=3,echo=2)

while True:
    print('Distance: ',sensor.distance*100)
    sleep(1)