#a program that queries the user for two strings and outputs the longer one

string1 = raw_input("Give the 1st string:")
string2 = raw_input("Give the 2nd string:")
if len(string1)>len(string2):
	print string1, "is longer"
if len(string1)<len(string2):
	print string2, "is longer"
if len(string1) == len(string2):
	print "The strings are of equal length"
