#tic tac toe
def insertMoves(board, listOfMoves):
	for items in listOfMoves:
		board[items[0]][items[1]]=items[2]			#inserting the value from matrix "moves" into the matrix "board"
		
	




row = [""] * 3
board = [row, row[:], row[:]]
moves = [ (0,0,"X"), (1,1,"O"), (1,0,"X"), (2,0,"O")]
insertMoves(board, moves)
print board