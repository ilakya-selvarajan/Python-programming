#A function that takes in tuple with name,height,weight and 'test height' as arg and to output a list with persons taller then test height.
def getTaller(listOfPeople, height):
	newList=[]
	for items in listOfPeople:
		if items[1]>175:				#the age in each tuple is checked if greater than 175
			newList.append(items)	
	return newList






person1 = ("John", 170, 69)
person2 = ("James", 180, 79)
person3 = ("Lisa", 163, 57)
person4 = ("Anne", 174, 55)
person5 = ("Peter", 195, 101)
personList = [ person1, person2, person3, person4, person5 ]
tallerList = getTaller(personList, 175)
print tallerList