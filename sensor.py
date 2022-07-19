from gpiozero import DistanceSensor
from time import sleep

td=20 #threshold distance in cm
t=15 #time for reading sensor
sensor = DistanceSensor(echo=18, trigger=17,max_distance=2, threshold_distance=0.2)
while True:
    d= sensor.distance *100 #distance in cm
    #condition to send alert
    if (d<=td):
        print('Full bin')
    else:
        print('Distance: ', round(sensor.distance * 100,3),sensor.when_out_of_range)
    sleep(t) #reads every t seconds