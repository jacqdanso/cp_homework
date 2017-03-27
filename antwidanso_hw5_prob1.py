#########################################################################################
#	Computational Physics HW5 Problem 1
#	
#	This program fits a cosine function to data of temperature variation in Munich as a 
#	of time. 
#
#	Written by Jacqueline Antwi-Danso 03/17
#########################################################################################
import numpy as np
from numpy import loadtxt, arange
from scipy.optimize import curve_fit
import pylab as plt
from pylab import plot, xlabel, ylabel, title, show

#read from txt file 
data = loadtxt("munich_t.txt", float)
x, y = data[:,0],data[:,1]

#mask bad data (50 determined by eye), isolate 2008 - 2012 values 
good_x, good_y, temp, years = [],[],[],[]

for i in arange(0,len(y)):
	if y[i] > -50 and y[i] < 50:
		good_y.append(y[i])
		good_x.append(x[i])

for j in arange(0, len(good_x)):
	if good_x[j] > 2008 and good_x[j] < 2012:
		temp.append(good_y[j])
		years.append(good_x[j])

#convert lists to arrays (see guess1)
temperature = np.array(temp)
time = np.array(years)

#parameter guesses, amplitude determined by eye 
guess_amplitude = 20
guess_phase = 0
guess_offset = np.mean(temperature)

p0 = [guess_amplitude, guess_phase, guess_offset]

#define cosine function
def my_cos(x, amplitude, phase, offset): 
	return np.cos(2*np.pi * x + phase) * amplitude + offset 

#fit data and generate an array of temp values based on guess params for comparison to fit
fit = curve_fit(my_cos, time, temperature, p0=p0)
data_fit = my_cos(time, *fit[0])
guess = my_cos(time, *p0)

#Plot best-fit model from 2008 to 2012
plt.plot(time, temperature,'.', color='black')
title('Munich Temperature Variation from 2008 to 2012')
xlabel('Time (Years)')
ylabel('Temperature ($^\circ$C)')
plt.plot(time, data_fit, label = 'Best-fit Model', color='blue', linewidth = 2)
plt.legend()
plt.show()

#Determine average temperatures predicted by model. Limits determined by eye 
lowest, highest = [], []
for k in arange(0,len(data_fit)): 
	if data_fit[k] < 1 and data_fit[k] > -1:
		lowest.append(data_fit[k])
	elif data_fit[k] > 19 and data_fit[k] < 21: 
		highest.append(data_fit[k])
		
print('Overall Average: ', np.mean(data_fit))
print('Coldest Average: ', np.mean(lowest))
print('Hottest Average: ', np.mean(highest))