#
from operator import itemgetter
mf = open("person.txt", "r")
allLines = mf.readlines()
items=[]
print "Select the criteria to sort the file by :"
print "1. Name"
print "2. Age"
print "3. Weight"
print "4. Height"
input = input("Sort by what criteria:")
for index, value in enumerate(allLines):
	allLines[index] = value.replace("\n","")
for line in allLines:
	myList = line.split(",")
	items.append(myList)
print sorted(items, key=itemgetter(input-1))

