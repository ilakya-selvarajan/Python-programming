#lowest common multiple(LCM)

a=input("Give A: ")
b=input("Give B: ")
myDict={(1,2):2}									#Initial assignment of one value in dictionary

def LCM(a,b):
	for i in range(a, a*b+1):
		if (i%a==0 and i%b==0):
			myDict[a,b] = i
			print "Not Found in dictionary!"
			print "LCM for A and B is", i
			return myDict

while a!=0 and b!=0:								#Checking if the two inputs are zero
	
	for key, value in myDict.iteritems():			#for every item in the dictionary
		if key==(a,b) or key==(b,a):				#checking if key already found
			print "Found in dictionary!"
			print "LCM for A and B is", value
			a=input("Give A: ")
			b=input("Give B: ")
			break									
			
	else:	
		LCM(a,b)									# If the values  not found in the dictionary, call function LCM
		a=input("Give A: ")
		b=input("Give B: ")
		
					
		
			
	
print "bye"

 


 
			

