#Pendulum Acceleromter
#Names: Tookie Wilson and Lily Keiderling
#Collecting Real World Data on Microbit

from microbit import *
import random

display.show(Image.BUTTERFLY) #display Butterfly when program is ready to begin
a= str(random.randint(1,999))
filename= "pendulum_data_" + a + ".txt" #assorted number in name lowers the odds of data overwriting

while not button_a.is_pressed(): #program runs when button_a is first pressed and concludes when button_a is pressed a second time
    sleep(10)

with open(filename, 'w') as file:
    sleep (1000)
    display.show(Image.HAPPY) #display smiley face when program is running
    time0 = running_time()
    while not button_a.is_pressed():
        elapsed_time = running_time()- time0;
        accel_x = accelerometer.get_x()
        accel_y = accelerometer.get_y()
        accel_z = accelerometer.get_z()
        accel_pendulum = str(elapsed_time) + "\t" + str(accel_x) + "\t" + str(accel_y) + "\t" + str(accel_z) + "\n" #recorded data stores in txt file, separated by tabs
        file.write(accel_pendulum)

    display.show(Image.TARGET) #display target when program concludes

file.close()