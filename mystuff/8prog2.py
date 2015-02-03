# A function to get unique items
def uniqueItems(list1, list2):
	newSet = set(list1+list2)		#set removes duplicates
	return list(newSet)				# returning the list


l1 = [1,2,1,3]
l2 = [2,3,4,5]
l3 = uniqueItems(l1,l2)
print l3