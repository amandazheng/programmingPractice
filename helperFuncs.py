## Helper functions for `8queens.py` program
## Author: Haard
##	H: annotation

QUEEN = 'Q'
TAKEN = '-'
EMPTY = '0'

def printBoard(queenList):
	# Generate empty board and mark all as taken
	board = [[TAKEN for x in range(8)] for y in range(8)]

	for q in queenList:
		board[q.x][q.y] = QUEEN

	for row in board:
		for elem in row:
			print(elem,end=' ')
		print()