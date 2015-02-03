# A function to remove integers from a list and move it to a new list
def parseIntegers(mixedList):
	newList=[]								#Initialising new list
	for value in mixedList:
		if isinstance(value,int)==True:		#if the value is an integer, it enters the loop
			if isinstance(value,bool):		#since True and False are also taken as integers, a if loop to check for the presence of bool
				continue
			else:
				newList.append(value)		#integers are appended in a new list
	return newList
		




testList = [1, 3,"abc", 5, True, 3.2, False, "Hello ", 7]
print parseIntegers(testList)