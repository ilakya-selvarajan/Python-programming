# Counting the number of vowels and storing in a dictionary
from __future__ import division
def vowelProportions (str):
	mydict={}
	vowels=['a','e','i','o','u','y']			#Assigning a list with vowels
	for letters in vowels:						
		count=str.count(letters)				#Counting the vowels in the string	
		percentage=int((count/len(str))*100)	
		mydict[letters] = percentage			#key=letter and %=value
	return mydict






print vowelProportions("aaccfedubbbyyyy")