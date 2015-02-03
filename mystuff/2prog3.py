# a program that queries the user for a two word string separated with a space, and outputs the latter word. 
string = raw_input("Enter a two word sentence:")
print "The second word is", string[string.find(" ")+1:]     #find() will give the position of space.