# A function to calculate the sum of the matrix
def matrixSum(m):
	sum=0
# first loop iterates through lists in list m
	for row in m:
# second loop iterates through items in row
		for value in row: 
			sum=sum+value
	return sum



myMatrix = [ [1,1,1,1], [2,2,2,2], [3,3,3,3], [2,2,2,2] ]
print matrixSum(myMatrix)