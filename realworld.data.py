#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:31:44 2019

@author: Lily
"""
import math
import matplotlib.pyplot as plt
import scipy.signal as sig
import numpy as np

###############################################################################
'''PARSING'''

fin = open('pendulum_data_580.txt') # as long as the file and the code is used from the same place (desktop, github, etc.) the code will work)

list_lines = []
time = []
accelX = []
accelY = []
accelZ = []
angle = []
i = 0


for line in fin:
    time.append(int(line.split("\t")[0]))
    accelX.append(int(line.split("\t")[1]))
    accelY.append(int(line.split("\t")[2]))
    accelZ.append(int(line.split("\t")[3]))
    angle.append(math.atan2(-1*accelX[i], accelY[i]))
    i = i+1

###############################################################################
'''ANALYSIS OF REAL-WORLD DATA'''

time = np.array(time)/1000  # time array

# filtering_data to clean up noisy graphs
angle_filtered = sig.medfilt(angle, 15)

# finds peaks of the filtered angle data
angle_pks, _ = sig.find_peaks(angle_filtered)

# function that calculates the average period
def calculating_avg_period(pks):    # pks is the pks array correlating to the graph that you want to find the period of
    pks_time = []
    period = []
    j = 0
    k = 1
    
    for j in range(len(pks)):
        pks_time.append(time[pks[j]])
        j = j + 1                                   # list of time of the peaks
    print("The Time of the Peaks: ", pks_time)      # prints all the peaks' times

    while k < len(pks_time):
        if abs(pks_time[k] - pks_time[k-1]) > 0.5:       # uses only peaks that are not too close together
            period.append((pks_time[k] - pks_time[k-1])) # creates a list of all the periods
        k = k + 1
        
    total = 0    
    for g in period:                    # sums the periods together
        total = total + g
    average_period = total/len(period)  # divides total by length of the period to get an average
    
    return average_period


print("The Average Period is ", calculating_avg_period(angle_pks))


###############################################################################
'''PLOTTING THE DATA (UNFILTERED AND FILTERED)'''

# Angle Graph
plt.figure()
plt.plot(time, angle, 'k-')
plt.xlabel('Time (seconds)')
plt.ylabel('Angle')
plt.title('Angle vs Time')
plt.xlim((0,6))
plt.show()

# Angle Filtered Graph
plt.plot(time, angle_filtered, 'k-', time[angle_pks], angle_filtered[angle_pks], 'b.') 
plt.xlabel('Time (seconds)')
plt.ylabel('Filtered Angle')
plt.title('Filtered Angle vs Time')
plt.xlim((0,6))
plt.show()

plt.figure(figsize=(6.5, 7))