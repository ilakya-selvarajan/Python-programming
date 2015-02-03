#Rotating pattern
bitPattern=raw_input("Give a bit pattern: ")
direction=raw_input("Give direction (left / right): ")
steps=input("Give number of steps: ")

	
def rotateLeft(bitPattern):
	number=bitPattern[steps:]	#contains all the digits after steps 
	number2=bitPattern[0:steps] #contains all the digits till step
	print number+str(number2)	
def rotateRight(bitPattern):
	number=bitPattern[0:len(bitPattern)-steps]
	number2=bitPattern[len(bitPattern)-steps:len(bitPattern)]
	print number2+str(number)
	

		

if direction=='left':
	rotateLeft(bitPattern)
else:
	rotateRight(bitPattern)	

