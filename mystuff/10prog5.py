# Random name generator
import random
def generateGroup(sizeOfGroup):
	newList2=[]
	random1=[]
	mf = open("persons.txt", "r")
	allLines = mf.readlines()
	for line in allLines:
		myList = line.split(",")
		newList2.append(myList[0])
	for i in range (0,sizeOfGroup):
		random1.append(random.choice(newList2))
	return random1	
		
group = generateGroup(4)
print group