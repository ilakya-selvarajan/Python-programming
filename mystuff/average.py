# Calculate the avg of list
def listAvg(lst):
# variable for avg
avg = 0.0
# iterate through list
for item in lst:
avg = avg + item
# return average
return avg / len(lst)