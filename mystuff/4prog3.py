#a program that queries the user for a number N, and the proceeds to output all powers of two smaller than N
input = input("Enter a number:")
i=0
j=0
while i<input:
	print pow(2,j)
	j=j+1
	i=pow(2,j)	
	