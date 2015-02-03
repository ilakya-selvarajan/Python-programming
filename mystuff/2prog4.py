# A program that queries the user for two strings, and proceeds to output the number of times the string can be found in another string

string1 = raw_input("Give the first string:")
string2 = raw_input("Give the second string:")
print "The first string can be found", string2.count(string1), "times in the second string."   #count() counts the no. of occurance of a substring
print "The second string can be found", string1.count(string2), "times in the first string."


