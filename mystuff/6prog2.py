# A function that calculates and returns the average of all items in the list m. 
from __future__ import division				#To output the decimal value
def average(m):
	sumOfList=0								#Initialising a variable named sumOfList				
	for i in range(0,len(m)):
		sumOfList+=m[i]						#Adding each number in the list in sumOfList
	return sumOfList/len(m)					# Returning the average
	
	
myList = [2,4,6,8,10,13]
print average(myList)
	
