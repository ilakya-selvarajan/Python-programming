#
def parsePersons(programFile):
	mf = open("persons.txt", "r")
	items=[]
	newList=[]
	newList1=[]
	newList2=[]
	myDict={}
	allLines = mf.readlines()
	for index, value in enumerate(allLines):
		allLines[index] = value.replace("\n","")
	for line in allLines:
		myList = line.split(",")
		newList2.append(myList[0])
		da=myList[1],myList[2],myList[3]
		newList1.append(da)
	myDict = dict(zip(newList2[0::2], newList1[1::2]))
	return myDict


lst = parsePersons("persons.txt")
print lst
	