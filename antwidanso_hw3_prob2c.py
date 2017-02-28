#########################################################################################
#	Computational Physics HW3 Problem 2 c
#	
#	This program accepts user-specified coefficients of a quadratic equation and calculates 
#	its roots using the appropriate method 
#	
#	INPUT:
#	a,b,c ---> coefficients 
#
#   	OUTPUT:
#	x1, x2 --> roots 
#	
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from math import sqrt 
from decimal import getcontext, Decimal 

# take user input 
a = float(input("Enter quadratic term coefficient : "))
b = float(input("Enter linear term coefficient : "))
c = float(input("Enter constant term coefficient : "))

#check difference between b and discriminant 
diff = b - sqrt((b**2) - 4*a*c)

if diff > 10**(-3): 

	#calculate both roots with formula 1 
	x1 = (-1*b + sqrt((b**2) - 4*a*c))/(2*a)
	x2 = (-1*b - sqrt((b**2) - 4*a*c))/(2*a)

else: 

	#calculate root 2 using formula 1 and root 1 using formula 2 
	x1 = (2*c)/((-1*b) - sqrt((b**2) - 4*a*c))
	x2 = (-1*b - sqrt((b**2) - 4*a*c))/(2*a)

#output 
print("The roots are",x1,"and",x2)
