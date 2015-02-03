#Random function
import random
input = input("Enter a number")
l=[]
print input
for i in range (1,input+1):
	l.append(random.randint(1,100))
print l