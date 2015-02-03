import random
def minimumMaximum(integerList):
	integerList.sort()
	l1=(integerList[1],integerList[-1])
	return l1





l = []
for i in xrange(random.randint(15,25)):
  l.append(random.randint(-150,150))
           
print "List:", l
print "Minimum and maximum:",minimumMaximum(l)