#a program that queries the user for number, and proceeds to output whether the number is an even or an odd number. 
number=1
while number!=0:
	number = input("Enter a number or a zero to quit:")
	if number%2==0 and number!=0:
		print "That's an even number"
		continue
	if number%2==1:
		print "That's an odd number"
		
if number==0:
	print "bye"
		
		