#card module
import random
def getDeck():
	numbers = 4*range(1,14)
	suit =  13*['Spade','Heart','Diamond','Club']
	deck = zip(numbers,suit)
	return deck

def shuffle(deckOfCards):
	for i in range(0, len(deckOfCards)-1):
		# pick an element in x[:i+1] with which to exchange x[i]
		j = int(random.random() * (i+1))
		deckOfCards[i], deckOfCards[j] = deckOfCards[j], deckOfCards[i]
	return deckOfCards

def deal(deckOfCards,number):
	selected_Cards=[]
	for i in range (0,number):
		selected_Cards.append(deckOfCards[i])
		del deckOfCards[:i]
		
	return selected_Cards
	
def output(listOfCards):
	for cards in listOfCards:
		if cards[0]==1:
			print "A of", cards[1]
		elif cards[0]==11:
			print "J of", cards[1]
		elif cards[0]==12:
			print "Q of", cards[1]	
		elif cards[0]==13:
			print "K of", cards[1]
		else:
			print cards[0],"of", cards[1]






