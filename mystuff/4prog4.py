#a program that queries the user for a string, and proceeds to generate a new string with all of the letters from the original string that are in upper case.
input = raw_input("Enter a string:")
result=""
for i in range (0,len(input)):
	if input[i].isupper() == True:
		result+= input[i]
print result