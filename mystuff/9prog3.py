#
from __future__ import division
def rowAverageSum():
	mf = open("matrix.txt", "r")
	matrix = []
	sum=0
	average=0
	allLines = mf.readlines()
	for index, value in enumerate(allLines):
		allLines[index] = value.replace("\n","")
	for row in allLines:
		matrix.append(row.split(" "))
	for row in matrix:	
		for values in row:	
			sum+=int(values)
		avg=sum/len(row)
		sum=0
		average+=avg
	return average
	mf.close()

print rowAverageSum()