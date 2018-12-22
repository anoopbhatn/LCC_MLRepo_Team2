import random
import math

clow = 96 #minimum chest length
chigh = 130 #maximum chest length
hlow=73 #minimum height
hhigh=82 #maximum height

XY=[] #List of all random tuples
C=[]  #List of randomly initializes Centroids
index=[] #ndex representing which centroid each tuple belongs toI

#Function to randomly initialize Data Samples and Centroids
def initialize(XY,C,datanum,k):
	X=[random.uniform(clow,chigh) for i in range (datanum)]
	Y=[random.uniform(hlow,hhigh) for i in range (datanum)]
	cX=[random.uniform(clow,chigh) for i in range (k)]
	cY=[random.uniform(hlow,hhigh) for i in range (k)]	
	
	for i in range (datanum):
		XY=XY+[(X[i],Y[i])]
	for i in range (k):
		C=C+[(cX[i],cY[i])]
	
	return XY,C

#Function to assign a centroid to each data sample
def allocateCentroid(XY,C,index,datanum,k):
	for i in range (datanum):
		index.append(0)
	for i in range (datanum):
		min = 99999
		for j in range 	(k):
			dist = math.sqrt((XY[i][0] - C[j][0])**2 + (XY[i][1] - C[j][1])**2)
			if dist<min:
				min = dist
				index[i]=j
	return index			

#Function to change the position of each centroid by finding the average of the samples belonging to each centroid
def moveCentroid(XY,C,index,datanum,k):
	for i in range (k):
		x=0
		y=0
		count=0
		for j in range (datanum):
			if index[j]==i:
				x=x+XY[j][0]
				y=y+XY[j][1]
				count=count+1
		x=x/count
		y=y/count
		C[i]=(x,y)
	
	return C
	
#Function to perform K Means Algorithm the required number of iterations
def runKmeans(iterations,XY,C,index,datanum,k):
	for i in range (iterations):
		index=allocateCentroid(XY,C,index,datanum,k)
		C=moveCentroid(XY,C,index,datanum,k)
		print("Iteration "+str(i+1)+":")
		print(C)
		print("-------------------------------------------------------------")
	return index,C


datanum = int(input("Enter number of samples:")) #Inputting number of Random data samples required
k = int(input("Enter number of centroids:"))	#Inputting number of Cluters required
iterations = int(input("Enter number of iterations:")) #Inputting number of iterations required

#Initializing the Data samples and the Centroids
XY,C=initialize(XY,C,datanum,k,)
#Running the K Means Algorithm
index,C=runKmeans(iterations,XY,C,index,datanum,k)
