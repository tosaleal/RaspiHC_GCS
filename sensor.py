from gpiozero import DistanceSensor
from time import sleep

sensor = DistanceSensor(echo=18, trigger=17,max_distance=2, threshold_distance=0.2)
while True:
    print('Distance: ', sensor.distance * 100)
    sleep(1)