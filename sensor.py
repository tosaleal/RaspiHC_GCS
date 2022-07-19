from gpiozero import DistanceSensor
from time import sleep

#pin definition
trig = 2
echo = 3

sensor = DistanceSensor(3,2)

while True:
    print('Distance: ',sensor.distance*100)
    sleep(1)