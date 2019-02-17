##	H:	Annotated by Haard Shah
##	H: 	brief analysis:
'''
The code gets stuck at the following board because of scoping error inside gameStatus(): (FIXED)
	- - - - - - - Q 
	Q Q Q Q Q Q Q - 
	- - - - - - - - 
	- - - - - - - - 
	- - - - - - - - 
	- - - - - - - - 
	- - - - - - - - 
	- - - - - - - - 
Suggestions/questions:
- moveQueen() function needs to be refined to do more exhaustive check before making a self.correct = True
- use the attached `printBoard` func to visualize
Questions:
- How can the eventual correct solution be modified to find ALL 92 solutions to the 8-queens problem?
'''
from helperFuncs import printBoard

# class for the queens 
# function for checking
# while loop for repeating

queenList = []
check = True

class queen():
    '''class for all queens'''
    def __init__(self, x, y, correct):
        self.x = x
        self.y = y
        self.correct = correct
    
    # to loop through the queens and move the queen when needed
    def moveQueen(self, queenNum):
        for b in range(8):
            if b != queenNum:
            	##	H: checking that no other queen is in the same row
            	##	H: (suggestion) should also check that no other queen is in the same column (not sure the code does that)
                if self.x == queenList[b].x: 
                    self.x += 1
                    print("moved x")
                    print( self.x)
                    print(self.x - 1)

                if self.y == queenList[b].y: 
                    self.y += 1
                    print("moved y")
                    print( self.y)
                    print(self.y - 1)

                ##	H: checking for IMMEDIATE diagonals (not sure if in all 4 directions)
                ##	H: (suggestion) need to check ALL diagonals not just neighboring ones
                if (self.x - 1) == queenList[b].x and (self.y - 1) == queenList[b].y:
                	## 	H: seems this block is trying to "move diag", should this be `self.y += 1`??
                    self.x += 1
                    print(self.x - 1)
                    print("moved diag")	
                else:
                	##	H: (suggestion) I don't think above 2 conditions are exhaustive to allow us to KNOW `correct` position
                    self.correct = True
                    print("true")
 	
 	##	H: to print object summary
 	##	H: now the object can be printed directly ex: `print(queen(0,0,False))`
    def __repr__(self):
    	return ", ".join([str(self.x), str(self.y), str(self.correct)])

#to check if the game is done yet
##	H: `check` has local scope here and is destroyed when function exists. THIS WAS THE CAUSE OF INFINITE LOOP
def gameStatus():
	##	H: following global statement is required to tell the function to refer to the global `check` variable
	global check
	for b in range(8):
		if queenList[b].correct == False: 
			break
	check = False

# to make list of queens
##	H: this puts queens everywhere on the 0th row of the matrix
for a in range(8):
    queenList.append(queen(0, a, False))

#begins while loop for checking
jj = 0
while check == True: 
	##	H: print iteration number
	print("iter = " + str(jj))
	for c in range(8): 
		if queenList[c].correct == False: 
			print("c = " + str(c))
			queenList[c].moveQueen(c)
		##	H: added to visualize the board (function attached as a separate file `helperFuncs.py`)
		printBoard(queenList)

	##	H: Added to stop infinite loop after 1 iteration (FIXED: but could still be useful to view intermediate steps)
    # if (jj >= 1):
    # 	exit()
    # jj += 1

	gameStatus()