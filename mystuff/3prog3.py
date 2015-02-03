#a program that queries the user for three numbers and outputs the smallest of them.

firstNumber = input("Give the 1st number:")
secondNumber = input("Give the 2nd number:")
thirdNumber = input("Give the 3rd number:")
#a = sorted([firstNumber,secondNumber,thirdNumber])
#print a[0], "is smallest ."


if firstNumber<secondNumber:
	if firstNumber<thirdNumber:
		print firstNumber, "is the smallest"
if  secondNumber<thirdNumber:
	if secondNumber<firstNumber:
		print secondNumber, "is the smallest"
if thirdNumber<firstNumber:
	if thirdNumber<secondNumber:
		print thirdNumber, "is the smallest"