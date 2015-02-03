#ROT-13
def rot13(string):
	decoded=''
	for i in range(0,len(string)):
		if ord(string[i])>ord('m'):			#ord('a')  prints 97 
			temp=chr(ord(string[i])-13)		#chr(97) prints 'a'. 
		else:
			temp=chr(ord(string[i])+13)		
		decoded+=temp
	return decoded
l="hello"	
print l
print(rot13(l))
print(rot13(rot13(l)))
print l