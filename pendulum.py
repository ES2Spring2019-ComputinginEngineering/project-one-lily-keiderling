import math
import numpy as np
import matplotlib.pyplot as plt


L= 7 #m
g= 9.8 #m/s^2
m = 0.6 #kg
theta= 60
theta_max <= 180 # degrees
theta_r =math.radians(theta)

def system_update(T, acc_t, vel_t, theta, t1, t2):
    dt= t2-t1
    T= ((2*math.pi) *(math.sqrt(L/g)))* dt
    theta= theta_max (g* math.radians(theta)) /m


def update_system(acc,pos,vel,time1,time2):
    # position and velocity update below
    dt = time2-time1
    posNext = pos+vel*dt+1/2*acc*dt
    velNext = vel+acc*dt
    return posNext,velNext

def print_system(time,pos,vel):
    print("TIME:     ", time)
    print("POSITION: ", pos)
    print("VELOCITY: ", vel, "\n")

# initial conditions
pos = [0]
vel = [0]
acc = [0,1,2,3,4,4,2,2,1,0,0,0,0,-1,-1,-2,-2,-2,-3,-4,-4]
time = np.linspace(0,20,21)  #time steps
print_system(time[0],pos[0],vel[0])

i = 1
while i < len(time):
    # update position and velocity using previous values and time step
    posNext, velNext = update_system(acc[i],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    print_system(time[i],pos[i],vel[i])




