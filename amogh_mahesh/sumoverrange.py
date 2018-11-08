'''
Created on 8 Nov , 2018
By @amogh_mahesh
program to sum all the integers between two given numbers
'''

#Inputting Start Vaue
start_value=int(input("Enter the start value\n"))
#Inputting End Vaue
end_value=int(input("Enter the end value\n"))
result=0

#Iterating through all the integers bw start and value and summming them
for i in range(start_value,end_value+1):
	result+=i

#Printing out the Result
print("Result="+str(result))
