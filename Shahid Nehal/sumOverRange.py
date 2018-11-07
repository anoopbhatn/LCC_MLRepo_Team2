''' Program to find the sum of numbers in the given range
	@Author : Shahid Nehal A

	Input : A start variable A and an end variable B representing the range [A, B]
	Output : The sum of all integers between A and B(inclusive)
'''

#start variable
A = int(input("Enter the start variable: "))
B = int(input("Enter the end variable: "))

#initializing the sum to 0
sum = 0

#computing the sum by simply iterating through the range of numbers from A to B (inclusive)
for num in range(A, B+1):
	sum += num

print ("The sum of numbers in the range [", A, ",", B, "] is", sum)
