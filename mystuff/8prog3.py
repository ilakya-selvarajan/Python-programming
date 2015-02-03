# Converting dictionary into tuple
def dictToList(dict):
	tuples = dict.items()		#converting dictionary into a list of tuples
	return tuples
	
dict = {0 : "abc", 2 : "bcd", 3: "cde", 4 : "def"}
myList = dictToList(dict)
print myList