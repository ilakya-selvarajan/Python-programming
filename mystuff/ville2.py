import random
from fractions import Fraction
a=[]
b=[]
def getNumbers(listOfFractions):
	j=0
	for i in listOfFractions:
		myFrac=i
		a.append(myFrac.numerator)
		b.append(myFrac.denominator)
	tuple=(a,b)
	return tuple
	
	

	
frac = []
for i in range(random.randint(10,15)):
    f = Fraction(random.randint(1,5), random.randint(2,8))
    frac.append(f)
    
print "List of fractions:", frac
num,den=getNumbers(frac)
print "Numerators:", num
print "Denominators:", den