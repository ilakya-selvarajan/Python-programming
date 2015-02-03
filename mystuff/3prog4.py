# parity bit 
bitInput = raw_input("Give a bit pattern:")
temp = bitInput.count("1")
if temp%2==0:
	print "Parity bit added: 1" + bitInput 
if temp%2==1:
	print "Parity bit added: 0" + bitInput 

