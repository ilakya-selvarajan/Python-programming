#a program that queries the user for a number N, and then proceeds to output all numbers between (-N and N)
number = input("Enter a number:")

for i in range(-number,number+1):
	print i
	