#Creating dictionary with person names and ages 
myDict={}
nameInput=raw_input("Enter a name or an empty string to stop:")
ageInput=input("Enter age:")
while len(nameInput)!=0 and isinstance(ageInput,int)==True:
	myDict[nameInput] = ageInput
	nameInput=raw_input("Enter a name or an empty string to stop:")
	if len(nameInput)==0:		#breaks when the name is empty
		break
	ageInput=input("Enter age:")
	
print myDict


