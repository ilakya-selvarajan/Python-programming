# A function which returns the largest of the values in a list
def maximumValue(myList):
	myList.sort()				#Sorts the list
	return myList[-1]			#Returns the last number in the list
	
n = [1,5,3,1,10,4,2,3]
print maximumValue(n)