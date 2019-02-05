# class for the queens 
# function for checking
# while loop for repeating

xCor = [0,0,0,0,0,0,0,0]
yCor = [0,0,0,0,0,0,0,0]
queenList = []

class queen():
    '''class for all queens'''
    def __init__(self, x, y, correct):
        self.x = x
        self.y = y
        self.correct = correct
        self.checkCorrect()
    
    def checkCorrect(queenNum):
        for b in range(8):
            if b != queenNum:
                if self.x == queenList[b].x: 
                    self.x += 1
                    print("moved x")
                if (self.x - 1) == queenList[b].x and (self.y - 1) == queenList[b].y:
                    self.x += 1
                    print("moved diag")

            


# to make list of queens
for a in range(8):
    queenList.append(queen(0, a, False))
    print(queenList[a].y)

check = True

while check == True: 
    for c in range(8): 
        if queen[c].correct = False: 
            queen[c].checkCorrect(c)
