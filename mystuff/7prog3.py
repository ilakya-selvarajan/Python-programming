# A function which gets a tuple with name and age and returns a new tuple with first letter of the name capitalized 
def capitalizeName(nameAgeTuple):
	newTuple=()								
	name=''				
	for value in nameAgeTuple:				
		if isinstance(value,str)==True:		#checks if the value is string
			name= value[0].upper()			#changes the first character of the string to captial
			for i in range (1,len(value)):	
				name=name+value[i]			#adds the rest of the character of the string to the new variable 'name'
	newTuple=(name,value)
	return newTuple
				



test = ("john ", 32)
print capitalizeName(test)