'''
Created on Thu Nov  8 12:34:32 2018
@author: prasada
input:two integers one is starting value and the ending value
output:The sum of all the integers in the given range
program to find the sum of all the integers in the given range(a,b),where a is starting integer and b is the ending integer.
'''
#initializing a variable to 0
sum=0
#assigning start value to a variable
start=int(input("start value"))
#assigning end value to a variable
end=int(input("end value"))
#for loop to calculate the sum of all the integers in the given range
for i in range(start,end+1,1):
    sum+=i
#printing the result
print(sum)
