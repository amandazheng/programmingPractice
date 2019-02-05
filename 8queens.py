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
                if self.x == queenList[b].x: 
                    self.x += 1
                    print("moved x")
                    print( self.x)
                    print(self.x - 1)

                if (self.x - 1) == queenList[b].x and (self.y - 1) == queenList[b].y:
                    self.x += 1
                    print(self.x - 1)
                    print("moved diag")
                else: 
                    self.correct = True
                    print("true")
    
    
#to check if the game is done yet
def gameStatus():
    for b in range(8):
        if queenList[b].correct == False: 
            break
    check = False

# to make list of queens
for a in range(8):
    queenList.append(queen(0, a, False))

#begins while loop for checking
while check == True: 
    for c in range(8): 
        if queenList[c].correct == False: 
            queenList[c].moveQueen(c)
    gameStatus()