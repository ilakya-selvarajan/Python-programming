def displayBoard(board):
    brd=""
    for i in range(0,3):
        for j in range(0,3):
            brd=brd + "[" + str(board[i*3+j]) + "]" #this will creat three square brackets with a value inside of (i*3+j)
        brd=brd+"\n"    #a new line will will follow after this to repeat the creation of another three square brackets
    print brd           # a total of 9 square brackets, three in one line, with a value from 1 to 9 will be displayed


def calculate(board,plr):
    reslt=-1
    winseq=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[0,4,8],[2,5,8],[1,4,7],[2,4,6]] #these are list of winning sequences

    for seq in winseq:
        if board[seq[0]]==board[seq[1]]==board[seq[2]]:#winner found
            if(plr%2==0):#First player
                reslt=1
            else:
                reslt=2
            break
    if plr==8:#end of game,draw
        reslt=0
    return reslt
    
player1=raw_input("Enter first player name  ")
s1=raw_input("Select sign, (X or O)? ")
player2=raw_input("Enter second player name  ")

if(s1=="X" or "x"):
    s2="O"
elif (s1=="O" or "o"):
    s2="X"
print "Welcome,",player1,"(",s1,") and",player2,"(",s2,")"
playagain=True
while(playagain):
    scoreBoard=["1","2","3","4","5","6","7","8","9"]

    for i in range(0,9):
        if(i%2==0):#it is player1's round
            displayBoard(scoreBoard)
            inpt=input(player1+" select the box number ")
            scoreBoard[inpt-1]=s1
        else:
            displayBoard(scoreBoard)
            inpt=input(player2+" select the box number ")
            scoreBoard[inpt-1]=s2
        result=calculate(scoreBoard,i)
        if(result==0):#It is a draw
            displayBoard(scoreBoard)
            print "It is a draw!\n"
            break;
        if(result==1):#player1 wins
            displayBoard(scoreBoard)
            print "Congratulations ",player1,"!, you won.\n"
            break;
        elif(result==2):#player2 wins
            displayBoard(scoreBoard)
            print "Congratulations ",player2,"!, you won.\n"
            break;
        #Else continue
    ch=raw_input("Do you want to play again? (Y/N) ")
	if(ch=="N" or ch=="n"):
		playagain=False
	