# A function to find min, max and average value
from __future__ import division
def minMaxAvg(dict):
	sum=0
	myTuple=()
	myValues= dict.values()						#extracting the values
	for values in myValues:	
		sum+=values				
	avg=sum/len(myValues)						#Calculating the average
	myTuple=(min(myValues),max(myValues),avg)	#Returning the min, max, and avg
	return myTuple




d = {"a":0, "b":-1, "c":3, "d":6, "e":11, "f":8}
print minMaxAvg(d)