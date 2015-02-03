#  A program that queries for two strings, and replaces all occurrences of the second string in the first string with their uppercase versions

string1 = raw_input("Give the first string:")
string2 = raw_input("Give the second input:")
string3 = string2.upper()												#changing into uppercase
print "Replaced string:", string1.replace(string2, string3)				#replacing string2 lowercases with uppercase in string1