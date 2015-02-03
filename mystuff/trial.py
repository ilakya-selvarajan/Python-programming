def removeDuplicates(n):
	for i in range(len(n) - 1, -1, -1):
		if n.count(n[i])>1:
			n.pop(i)
	return n


	
myList = [1, 2, 1, 3, 3, 2,-1, 5, 3, 5,-1, 2, 5]
removeDuplicates(myList)
print myList


