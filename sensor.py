from gpiozero import DistanceSensor
from time import sleep

threshold_distance=20
sensor = DistanceSensor(echo=18, trigger=17,max_distance=2, threshold_distance=0.2)
while True:
    d= sensor.distance *100 #distance in cm
    #condition to send alert
    if (d<=threshold_distance):
        print('Full bin')
    else:
        print('Distance: ', sensor.distance * 100,sensor.when_out_of_range)
    sleep(1)