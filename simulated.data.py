#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 15:20:08 2019

@author: Lily
"""

import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

###############################################################################
'''CREATING THE SIMULATED DATA'''

# initial conditions
l = int(input("The Length of the Pendulum (in meters): ")) # user can input their choice in length of pendulum in meters
g = -9.8 # m/s^2
pos = [math.pi/6] # radians
vel = [0] # rad/sec
accel = [(g/l) * math.sin(pos[0])] # rad/sec^2
time = np.linspace(0, 20, 20000) # time step


def update_system(accel,pos,vel,time1,time2):
    #angular position, velocity and acceleration update below
    dt = time2-time1
    posNext = pos + (dt*vel)
    velNext = vel + (dt*accel)
    accelNext = (g/l) * math.sin(posNext)
    return posNext,velNext, accelNext

i = 1
while i < len(time):
    # update angular position, velocity and acceleration using previous values and time step
    posNext, velNext, accelNext = update_system(accel[i-1],pos[i-1],vel[i-1],time[i-1],time[i])
    pos.append(posNext)
    vel.append(velNext)
    accel.append(accelNext)
    i = i + 1
    
###############################################################################
'''ANALYSIS OF SIMULATED DATA'''
# Find peaks of angular position
pos_array = np.array(pos) # turns pos into an array
pos_pks, _ = sig.find_peaks(pos_array) # finds peaks of pos array


# Calculating the Average Period
def calculating_avg_period(pks): # pks is the pks array correlating to the graph that you want to find the period of
    pks_time = []
    period = []
    j = 0
    k = 1
    total = 0

    for j in range(len(pks)):
        pks_time.append(time[pks[j]])
        j = j + 1                               # list of time of the peaks
    print("The Time of the Peaks: ", pks_time)  # prints all the peaks' times

    while k < len(pks_time):
        if abs(pks_time[k] - pks_time[k-1]) > 0.5:          # uses only peaks that are not too close together
            period.append((pks_time[k] - pks_time[k-1]))    # creates a list of all the periods
        k = k + 1
        
    for g in period:                        # sums the periods together
        total = total + g
    average_period = total/len(period)      # divides total of all the periods by length of the period list to get an average
    
    return average_period


print("The Average Period is ", calculating_avg_period(pos_pks)) # prints the average period


###############################################################################
'''PLOTTING THE GRAPHS'''

plt.figure(figsize=(6.5, 9))

# Angular Position Graph
plt.subplot(3,1,1)
plt.plot(time, pos, 'b--', time[pos_pks], pos_array[pos_pks], 'r.')
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Position (m)')
plt.title('Angular Position vs Time')
plt.xlim((0, 6)) # set x range to only graph the good data
plt.grid()

# Angular Velocity Graph
plt.subplot(3,1,2)
plt.plot(time, vel, 'r--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Velocity (m/s)')
plt.title('Angular Velocity vs Time')
plt.xlim((0, 20)) # set x range to only graph the good data
plt.grid()

# Angular Acceleration Graph
plt.subplot(3,1,3)
plt.plot(time, accel, 'g--') 
plt.xlabel('Time (seconds)')
plt.ylabel('Angular Acceleration (m/s^2)')
plt.title('Angular Acceleration vs Time')
plt.xlim((0, 20)) # set x range to only graph the good data
plt.grid()
plt.tight_layout()
plt.show()


###############################################################################
'''PLOTTING THE LENGTH VS PERIOD'''

# Length of Pendulum vs Period Graph
s = [0.207, 0.254, 0.278, 0.295, 0.335]
t = [0.772, 0.847, 0.985, 0.880, 1.044]
rs = [0.207, 0.254, 0.278, 0.295, 0.335]
rt = [0.940, 1.038, 1.085, 1.117, 1.189]

plt.plot(s, t, 'b.', label = 'Real World Data')
plt.legend()
plt.plot(rs, rt, 'r.', label = 'Simulated Data')
plt.legend()
plt.xlabel('Length of Pendulum (m)')
plt.ylabel('Period (1/sec)')
plt.title('Length of Pendulum vs Period Graph')
plt.show()








