# 	
def readProducts(filename):
	myDict={}
	items=[]
	f=open("products.txt","r")
	allLines = f.readlines()
	for index, value in enumerate(allLines):
		allLines[index] = value.replace("\n","")
	for line in allLines:
		myList = line.split(", ")
		for item in myList:
			items.append(item)
	myDict = dict(zip(items[0::2], items[1::2]))
	return myDict


dict = readProducts("products.txt")
print dict