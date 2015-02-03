#Addition of fractions
from fractions import Fraction
def fractionAvg(listOfFractions):
	addition=0
	for i in listOfFractions:
		addition = addition+Fraction(i)
	return addition






m = [Fraction(1,2), Fraction(1,4), Fraction(1,3)]
print fractionAvg(m)