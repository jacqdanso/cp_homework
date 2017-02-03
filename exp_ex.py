from numpy import exp 
from math import factorial 
from decimal import getcontext, Decimal 


getcontext().prec = 10

for x in range(0, 100,10):
	terms=[]
	for n in range(0,100):
		top=((-1)**n)*(x**n)
		bottom=factorial(n)
		num=Decimal(top/bottom)
		terms.append(num)
	print(sum(terms),'       ', exp(-x))
	


