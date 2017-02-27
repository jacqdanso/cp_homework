#########################################################################################
#	Computational Physics HW4 Problem 2 (b)
#	
#	This program uses a Monte Carlo procedure to evaluate the integral (x^(-1/2))/((e^x)+1)
#	
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from random import random 
from math import exp, sqrt

#function to be integrated 
def f(x): 
	return (x**(-1/2))/((exp(x)+1))

#weight function 
def w(x):
	return x**(-1/2)

#derived transformation function 
def x(z):
	return z**2

#probability distribution function 
def p(x): 
	return 1/(2*sqrt(x))

N = 10**6 
limit = 1
weighted_function = float(0)

for i in range(N): 	
	for i in range(limit):
		a = random()
		point = x(a)
		if a > point: 
			weighted_function += f(point)/w(point)
	
#calculate integral
I = (2/N)*weighted_function
print(I)
