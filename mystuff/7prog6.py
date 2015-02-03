#A function which gets as an argument a list of number tuples, and sorts the list into increasing order.
def sortList(tupleList):
	for i in range( 0,len(tupleList) ):
		for j in range(i+1, len(tupleList) ):
			if tupleList[j][0]*tupleList[j][1]<tupleList[i][0]*tupleList[i][1]:		
				temp=tupleList[j]
				tupleList[j]=tupleList[i]
				tupleList[i]=temp






myList = [(2, 3.0), (3, 1.0), (4, 2.5), (1, 1.0)]
sortList(myList)
print myList
