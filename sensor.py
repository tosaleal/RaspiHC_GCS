import gpiozero as gpio
from time import sleep

#pin definition
trig = 2
echo = 3

sensor = gpio.DistanceSensor(echo,trig)

while True:
    print('Distance: ',sensor.distance*100)
    sleep(1)