#########################################################################################
#	Computational Physics HW3 Problem 1
#	
#	This program reads from  stm.txt, which contains height values of a silicon surface, 
# 	and creates a density plot. 
#
#
#	Written by Jacqueline Antwi-Danso 02/17
#########################################################################################
from numpy import loadtxt
from pylab import imshow, show, colorbar, title, xlabel, ylabel

#read from txt file 
grid = loadtxt("stm.txt", float)

#make density plot 
imshow(grid, origin='lower')
title('Height density plot of silicon surface')
xlabel('X-coordinate')
ylabel('Y-coordinate')
colorbar()
show()
