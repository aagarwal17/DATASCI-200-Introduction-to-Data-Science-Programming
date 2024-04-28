class Board:
  def __init__(self, n, epiCenterNum):
    self.size = n
    self.theListBoard = [0] * n
    self.theListBoard[epiCenterNum] = 1
    print("Creating board: ", self.theListBoard)


  def move(self, cityNum):
    inspectNum = self.theListBoard[cityNum]
    print("Checking location:", cityNum, ", Value =", inspectNum)
    tempList = []
    for index, item in enumerate(self.theListBoard):
        if index == 0:
            if item > 0 or self.theListBoard[index+1] > 0:
                tempList.append(self.theListBoard[index] + 1)
            else:
                tempList.append(0)
        elif index == self.size - 1:
            if item > 0 or self.theListBoard[index-1] > 0:
                tempList.append(self.theListBoard[index] + 1)
            else:
                tempList.append(0)
        else:
            if item > 0:
                tempList.append(self.theListBoard[index] + 1)
            elif self.theListBoard[index+1] > 0 or self.theListBoard[index-1]:
                tempList.append(self.theListBoard[index] + 1)
            else:
                tempList.append(0)
    self.theListBoard = tempList
    print("New board: ", self.theListBoard)
    return inspectNum

# board = Board(10,2)
# print(board.size)
# board.move(0)
# board.move(1)
# board.move(2)