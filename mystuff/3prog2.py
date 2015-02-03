#a program that queries that takes in 4 character strings, and output whether the first string contains all letters of the second string in reverse order.
string1 =  raw_input("Give the 1st string:")
string2 =  raw_input("Give the 2nd string:")
string3 = string1[::-1]
if string2 == string3:
	print string1, "is", string2, "in reverse order!"
else:
	print string1, "is not", string2, "in reverse order!"