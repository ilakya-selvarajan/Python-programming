# To find the index of the second occurrence of string B in string A.

string1 = raw_input("Give the string A:")
string2 = raw_input("Give the string B:")
a = len(string2)
b = string1.find(string2)
d=a+b
c = string1[b+a:]
print c
print "The index of the 2nd occurrence of B in A is", c.find(string2)+d
