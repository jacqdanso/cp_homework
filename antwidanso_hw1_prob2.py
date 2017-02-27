#########################################################################################
#	Computational Physics HW1 Problem 2
#	
#	This program calculates the altitude of a satellite in a circular orbit around Earth 
#	with a user-specified periodic orbit time 
#	
#	Written by Jacqueline Antwi-Danso 01/17
#########################################################################################
from numpy import pi 
from fractions import Fraction 
from decimal import getcontext, Decimal 

# define constants
e_radius=6371e3
e_mass=5.97e24
grav_const=6.67e-11

# take user input 
time = float(input("Enter orbit time in seconds: "))

# reject negative integers 
if time < 0.0 : 
	print("Invalid entry.")
else :
	ex=Fraction('1/3')
	alt=(((grav_const*e_mass*(time**2))//(4*pi**2))**ex)-e_radius

# set the precision
getcontext().prec = 5
output=Decimal(alt)

print("Satellite altitude is :", output/Decimal(1e3),"km")
