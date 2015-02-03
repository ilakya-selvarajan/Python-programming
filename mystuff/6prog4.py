# A function which returns a new list with all the even numbers stored in the list.
def evenNumbers(myList):
	secondList=[]							#Initialising an empty list
	for i in range(0,len(myList)):
		if myList[i]%2==0:					
			secondList.append(myList[i])	#Append function to add the even numbers to a new list
	return secondList
	
n = range(1,11)
otherList = evenNumbers(n)
print otherList