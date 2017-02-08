#########################################################################################
#	Computational Physics HW2 Problem 2
#	
#	This program calculates the binding energy of an atomic nucleus given the atomic 
#	number and mass number 
#
#	INPUT
#	A: mass number 
#	Z: atomic number
#	
#	OUTPUT
#	B: binding energy per atom in MeV
#	B/A: binding enery per nucleon in MeV
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from math import sqrt

# take user input 
A = int(input("Enter mass number : "))
Z = int(input("Enter atomic number : "))

#define constants
a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

#define a5
if (A % 2) > 0 : #if A is odd
	a5 = 0.0
elif (A % 2) == 0 and (Z % 2) == 0 : #if both A and Z are even 
	a5 = 12.0
elif (A % 2) == 0 and (Z % 2) > 0 : #if A is even and Z is odd 
	a5 = -12.0 

#compute binding energy
term1 = a1*A
term2 = a2*A**(2/3)
term3 = a3*(Z**2)/A**(1/3)
term4 = a4*((A-(2*Z))**2)/A
term5 = a5/A**(1/2)

B = term1 - (term2) - (term3) - (term4) - (term5)

#output 
print("Atom binding energy :", '{:2.3f}'.format(B),"MeV")
print("Nucleon binding energy :", '{:2.3f}'.format(B/A),"MeV")


