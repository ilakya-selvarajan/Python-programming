#A function to remove duplicates
def removeDuplicates(n):
	for i in range(len(n) - 1, -1, -1):			#Reads the list from the last number
		if n.count(n[i])>1:						#Counts the numberof times the number is present
			n.pop(i)							
	#return n




myList = [1, 2, 1, 3, 3, 2,-1, 5, 3, 5,-1, 2, 5]
removeDuplicates(myList)
print myList



#don't have to return