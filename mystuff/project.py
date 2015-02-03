#tic tac toe
def welcome():
	print "Hi! Welcome to tic tac toe"
	print "Tic-tac-toe is a game for two players, X and O, who take turns marking the spaces in a 3*3 grid."
	
def player_assignment():
	pass
def default_array():
	list=['a']*8
	print list
	input= raw_input("Do you enter X or O")
	for i in range (0,8):
		list[i]=input
		print list
		if i==2:
			if list[0]==list[1]==list[2]:
				print "winner"
		elif i==
			elif list[3]==list[4]==list[5]:
				print "winner"
			elif list[6]==list[7]==list[8]:
				print "winner"
			elif list[0]==list[3]==list[6]:
				print "winner"
			elif list[1]==list[4]==list[7]:
				print "winner"
			elif list[2]==list[5]==list[8]:
				print "winner"
			elif list[0]==list[4]==list[8]:
				print "winner"
			elif list[2]==list[4]==list[6]:
				print "winner"
		input= raw_input("Do you enter X or O")		
def is_the_game_over():
	pass
	
	

	
welcome()
player_assignment()
default_array()
#player_move()
is_the_game_over()