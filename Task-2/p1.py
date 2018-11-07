'''
Created on Nov 1, 2018
@author: amogh_mahesh

Program to sum all the integer numbers in the give nrange
'''
#inputting start value
start_value=int(input("Enter the start value\n"))

#inputting end value
end_value=int(input("Enter the end value\n"))

#variable to store the final result
result=0

#a for loop to traverse through each number in the given range and add them
for i in range(start_value,end_value+1):
	res+=i

#Printing out the result
print("Result="+str(res))

