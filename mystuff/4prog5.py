#Permutation string
string1 = raw_input("Enter string A: ")
string2 = raw_input("Enter string B: ")
counter=0
if len(string1)==len(string2):
	for i in range (0,len(string1)):
		if string1.count(string1[i]) == string2.count(string1[i]):
			counter=counter+1
		else:
			break
else:
	print  string1, "is not a permutation of", string2

if counter==len(string1):
	print string1, "is a permutation of", string2
else: 
	print  string1, "is not a permutation of", string2