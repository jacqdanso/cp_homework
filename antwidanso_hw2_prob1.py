#########################################################################################
#	Computational Physics HW2 Problem 1(a)
#	
#	This program calculates the time in years that a spaceship takes to reach its 
#	destination with a user-specified distance and speed of the spaceship as a 
# 	fraction of the speed of light. 
#	
#	INPUT
#	x: distance to destination in ly 
#	v: velocity of spaceship as a fraction of c
#	
#	OUTPUT
#	t_[reference]: time to destination in years
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from math import sqrt

#define constants
c = 299792458.0

# take user input 
x = float(input("Enter destination distance in light years: "))
v = float(input("Enter spaceship velocity as fraction of c: "))

#convert distance in ly to distance in m , and convert v from fraction to number 
distance = x * 9.461 * (10 ** 15)
vel = v * c 

#calculate times in years for observers on earth and ship
gamma = 1/sqrt(1.0 - (v**2))
sec_to_yr = 3.154 * 10 ** 7
t_ship = distance/(vel * sec_to_yr)
t_earth = t_ship*gamma

#output 
print("Travel time perceived by observer on Earth :", '{:2.3f}'.format(t_earth),"years")
print("Travel time for spaceship passenger :", '{:2.3f}'.format(t_ship),"years")

