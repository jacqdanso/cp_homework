#########################################################################################
#	Computational Physics HW4 Problem 1
#	
#	This program simulates the decay of Bi-213 into Bi-209
#	Possible decay sequences - Bi-213 --> Tl-209 --> Pb-209--> Bi-209
#  							   Bi-213 --> Pb-209 --> Bi-209
#
#	Variable definitions:
#	NBi213 - number of Bi-213 atoms 
#	NPb - number of Pb-209 atoms 
#	NBi209 - number of Bi-209 atoms 
#	NTl - number of Tl-209 atoms 
#
#	t - total decay time in seconds
#	h = step size in seconds 
#
#   (these probabilities are of whether the atom decays or not)
#	pBi = probability of Bi-213 decay in one step 
# 	pPb = probability of Pb-209 decay in one step 
#	pTl = probability of Tl-209 decay in one step 
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from random import random 
from numpy import arange, copy 
import pylab
from pylab import plot, xlabel, ylabel, title, show

t = 2*(10**4)
h = 1

#probabilities 
pBi = 1 - 2**(-h/(46*60))
pTl = 1 - 2**(-h/(2.2*60))
pPb = 1 - 2**(-h/(3.3*60))

#number of atoms 
NBi213 = 10**4
NTl = 0 #initial number of Tl atoms 
NPb = 0 #initial number of Pb atoms
NBi209 = 0 #initial number of Bi-209 atoms

x = arange(0.0,t,h)
yBi213,yTl, yPb, yBi209  = [], [], [], []

for j in x:
	yBi213.append(NBi213)
	yTl.append(NTl)
	yPb.append(NPb)
	yBi209.append(NBi209)

	#Calculate number of Bi-213 atoms that decay 
	Bidecay = 0 
	for i in range(NBi213): 
		if random() < pBi: 
			Bidecay += 1	
	NBi213 -= Bidecay 
	if random() > 0.9791 and random() < 0.209:
		NTl += Bidecay 
	elif random() < 0.9791:
		NPb += Bidecay 
	
	#Calculate number of Tl-209 atoms that decay into Pb-209
	Tldecay = 0 
	for i in range(NTl): 
		if random() < pTl: 
			Tldecay += 1
	NTl -= Tldecay 
	NPb += Tldecay 
	
	#Calculate number of Pb-209 atoms that decay into Bi-209
	Pbdecay = 0 
	for i in range(NPb): 
		if random() < pPb: 
			Pbdecay += 1
	NPb -= Pbdecay 
	NBi209 += Pbdecay 

#Graph 
plot(x,yBi213, label = 'Bi-213')
plot(x,yTl, label = 'Tl-209')
plot(x,yPb, label = 'Pb-209')
plot(x,yBi209, label = 'Bi-209')
title('Bi-213 Decay as a function of time')
xlabel('Time (seconds)')
ylabel('Number of atoms')
legend = pylab.legend(loc='center right')
show()


