#A program to print if the length of the given string is between minLen and maxLen

def isValid(string, minLen, maxLen):
	
	if len(string)<=maxLen and len(string)>=minLen:
		print "True"
	else:
		print "False"


isValid("abcd", 2, 6)
