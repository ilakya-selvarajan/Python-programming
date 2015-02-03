# A function to merge two lists
def mergeLists(list1, list2):
	list3 = list1+list2			#Merging two lists
	list3.sort()				#Sorting the new list
	return list3
	
n = [1, 3, 5,7, 9]
m = [2, 4, 8, 12]
newList = mergeLists(n, m)
print newList