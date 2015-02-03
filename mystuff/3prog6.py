#a program that queries the user for a 4-bit binary string and decodes it into decimal number.

bitNumber = raw_input("Give a 4 - bit binary string:")

if bitNumber[0]=='0':
	fourthPlace=0
else:
	fourthPlace=pow(2,3)
if bitNumber[1]=='0':
	thirdPlace=0
else:
	thirdPlace=pow(2,2)
if bitNumber[2]=='0':
	secondPlace=0
else:
	secondPlace=pow(2,1)
if bitNumber[3]=='0':
	firstPlace=0
else:
	firstPlace=pow(2,0)
print bitNumber, "is", fourthPlace+thirdPlace+secondPlace+firstPlace, "as decimal number"  