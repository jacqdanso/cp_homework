# cp_homework
HW for Computational Physics Course 
Branch : HW3 

The programs in this branch explore the plotting capabilities and arithmetic limitations of Python. Their output is documented as .png and .txt files. 

#Problem 1 
antwidanso_hw3_prob1.py reads a grid of height and coordinate values of a silicon surface from a .txt file and makes a density plot of the surface. 

Output files: 
antwidanso_hw3_prob1.png - density plot 

Limitations :
The colorbar in antwidanso_hw3_prob1.png isn't labelled (couldn't get Python to do it). I'm hoping that it is implicit from the title that the color denotes the height of the surface. 

#Problems 2 and 3
antwidanso_hw3_prob2.py accepts the coefficients of a quadratic equation and returns its roots using two identical formulas. One notices a slight error depending on the magnitude of the disriminant. antwidanso_hw3_prob2c.py remedies this issue by checking the magnitude of the discriminant and using the appropriate formula (the cutoff is arbitrary). 

Output files:
antwidanso_hw3_prob2.png - screenshot of root values 
antwidanso_hw3_prob2.txt.rtf -response to question regarding reason for discrepancy

#Problem 4
antwidanso_hw3_prob3.py plots the heat capacity of 1000 cubic meters of Al as a function of temperature using Debye's theory of solids. 

Output file: 
antwidanso_hw3_prob4.png - heat capacity plot 
