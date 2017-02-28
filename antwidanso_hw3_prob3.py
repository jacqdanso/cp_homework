#########################################################################################
#	Computational Physics HW3 Problem 3 
#	
#	This program calculates the heat capacity of 1000 cubic meters of solid aluminium  
#	given its temperature 
#	
#	CONSTANTS:
#	vol = solid volume in cubic meters 
#	rho = number density of atoms per cubic meter 
#	bolt = Boltzmann constant in m^2 kg s-2 K-1
#	deb = Debye temperature in K 
#
#	INPUT:
#	T = temperature in K 
#
#  	OUTPUT:
#	cv - heat capacity of aluminium solid 
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from math import exp 
from pylab import plot, show, title, xlabel, ylabel

#define constants
vol = 10 ** (-3) 
rho = 6.022 * (10 ** 28)
bolt = 1.38064852 * (10 ** -23)
deb = 428

#define integral as function
def I(x):
	return ((x**4)*exp(x))/((exp(x)-1)**2)

#calculate integral using trapezoid rule and find cv(T) for T=5 to 500 K
N = 1000
a = 10**(-10) # to avoid dividing by 0
cv=[] #define array of heat capacity values 

for T in range(5,500):
	b = deb/T
	h = (b-a)/N 
	s = 0.5*I(a) + 0.5*I(b)
	
	for k in range(1,N): 
		s += I(a + (k*h))
	
	integral = h*s
	cv.append( 9.0 * vol * rho * bolt * ((T/deb)**3.0)*integral)

#plot graph for t between 5K and 500K
plot(cv)
title('Aluminium heat capacity as a function of temperature')
xlabel('Temperature (K)')
ylabel('$C_v$ (J/K)')
show()

	

