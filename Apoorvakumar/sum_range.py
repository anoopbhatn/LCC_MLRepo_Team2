''' Program to find the sum of all numbers in the given range [A,B]
   Created on November 08, 2018
  	@Author : Apoorva kumar P
  	Input : A start variable A and an end variable B representing the range [A, B]
  	Output : The sum of all integers from A and B(both inclusive)
'''


#initializing the variable to store sum
sum=0;
#inputing start value  
start = int(input("Enter Start value:"))
#inputing end value
end   = int(input("Enter End value:"))
#for loop to determine the sum of all integers in the range [A,B]
for i in range(start,end+1):
   sum=sum + i
#printing sum value
print(sum)  
