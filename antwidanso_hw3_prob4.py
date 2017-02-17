#########################################################################################
#	Computational Physics HW3 Problem 4
#	
#	This program uses Gaussian quadrature to calculate the integral of exp(x^2) from 0 
#	to 3 with a step size of 0.1 and plots the resulting array, E
#	
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
import numpy as np
from math import exp 
from pylab import plot, show, title, xlabel, ylabel
from numpy import ones,copy,cos,tan,pi,linspace

#copied from http://www-personal.umich.edu/~mejn/computational-physics/gaussxw.py
#python not allowing me to do from gaussxw import gaussxw 

def gaussxw(N):

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

#define function 
def f(x):
	return exp(x**2)

#to avoid any wonky behavior with floats, create frange function to mimic range
def frange(begin, end, step):
  while begin < end:
    yield begin
    begin += step

N = 30 #calculated using step size, h = 0.1 
a = 0.0
y = []

for i in frange(a,3.0,0.1): 
	b = i 
	x,w = gaussxw(N)
	xp = 0.5*(b-a)*x + 0.5*(b+a)
	wp = 0.5*(b-a)*w
	
	# Integrate
	s = 0.0
	for k in range(N):
		s += wp[k]*f(xp[k])

	val = copy(s)
	y.append(val)

#plot graph 
plot(y)
title('Plot of E(x)')
xlabel('x')
ylabel('E(x)')
show()