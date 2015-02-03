#A program that queries the user for numbers one at a time, and appends all the numbers entered into a list. 
list=[]														#Initializing an empty list
inputNumber=1
while inputNumber!=0:
	inputNumber = input("Enter a number or a zero to quit:")
	if inputNumber!=0:
		list.append(inputNumber)							#append function to add the input numbers into list
	else:													
		break
	
print list
