#########################################################################################
#	Computational Physics HW3 Problem 2 a, b
#	
#	This program accepts user-specified coefficients of a quadratic equation and calculates 
#	its roots using two equivalent methods 
#	
#	INPUT:
#	a,b,c ---> coefficients 
#
#   OUTPUT:
#	x1, x2 --> roots using formula 1
#	y1, y2 --> roots using formula 1
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from math import sqrt 
from decimal import getcontext, Decimal 

# take user input 
a = float(input("Enter quadratic term coefficient : "))
b = float(input("Enter linear term coefficient : "))
c = float(input("Enter constant term coefficient : "))

#calculate roots with formula 1 
x1 = (-1*b + sqrt((b**2) - 4*a*c))/(2*a)
x2 = (-1*b - sqrt((b**2) - 4*a*c))/(2*a)

#output 
print("With formula 1, the roots are",x1,"and",x2)

#calculate roots with formula 2 
y1 = (2*c)/((-1*b) - sqrt((b**2) - 4*a*c))
y2 = (2*c)/((-1*b) + sqrt((b**2) - 4*a*c))

#output 
print("With formula 2, the roots are",y1,"and",y2)




