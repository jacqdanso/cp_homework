#########################################################################################
#	Computational Physics HW1 Problem 1 (b) 
#	
#	This program converts a user-specified positive non-zero integer from decimal to binary notation. 
#	
#	Written by Jacqueline Antwi-Danso 01/17
#########################################################################################
import copy 
#take user input 
number = int(input("Enter a positive non-zero integer to be converted: "))

#reject zero and negative integers 
if number <= 0 : 
	print("Invalid entry.")
else :
	#calculate binary version using division by 2 
	rem_list=[] #initialize a list that will contain the remainders
	
	num=copy.copy(number) #copy user input into variable, num
	
	while num>0 :
		rem=num % 2			
		num=num//2
		rem_list.append(rem) #append remainders to list
			
	rem_list.reverse() #reverse order, since append adds to end of list
	output="".join(str(x) for x in rem_list)
	
	#output binary version of input 
	print("The binary representation of",number,"is:",output)
