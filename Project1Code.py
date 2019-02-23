import math
import numpy as np
#import matplotlib.pyplot as plt


# initial conditions
l = 1 #m
g = -9.8 #m/s^2
pos = [math.pi/6]
vel = [0]
accel = [(g/l) * math.sin(pos[0])]
time = np.linspace(0, 20, 20000)#time step


def update_system(accel,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos + (dt*vel)
    velNext = vel + (dt*accel)
    accelNext = (g/l) * math.sin(posNext)
    return posNext,velNext, accelNext

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext, accelNext = update_system(accel[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    accel.append(accelNext)
    print((pos[i],vel[i], accel[i]))
    i = i + 1


