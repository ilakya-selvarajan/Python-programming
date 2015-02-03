import random


# next line generates a random number
# and assigns it to variable n1
n1 = random.randint(50,150) 

def process(listOfValues, function):
    for index, value in enumerate(listOfValues):
        listOfValues[index] = function(value)
function = lambda x: x-1

testlist = []
for i in range(0, random.randint(10,15)):
    testlist.append(random.randint(-100,100))
    
print "List before:",testlist

process(testlist, function)
print "List after",testlist