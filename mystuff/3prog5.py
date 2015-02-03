#a program that queries the user for a string containing a DNA sequence, and proceeds to output the proportions of four nucleotide bases (A, C, G and T) as %
from __future__ import division
sequence = raw_input("Enter sequence:")
lengthOfSeq = len(sequence)
gContent = sequence.count("g")
tContent = sequence.count("t")
cContent = sequence.count("c")
aContent = sequence.count("a")
gPercentage = (gContent/lengthOfSeq)*100
tPercentage = (tContent/lengthOfSeq)*100
cPercentage = (cContent/lengthOfSeq)*100
aPercentage = (aContent/lengthOfSeq)*100
gWhole =int(gPercentage)
tWhole =int(tPercentage)
cWhole =int(cPercentage)
aWhole =int(aPercentage)
print "Proportion of A:", aWhole
print "Proportion of T:", tWhole
print "Proportion of C:", cWhole
print "Proportion of G:", gWhole