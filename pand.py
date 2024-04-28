from Board import Board
import random

class Solver:
  def __init__(self, Board):
    self.Board = Board

  def solve(self):
    highestNumFound = 0
    num1 = 0
    while highestNumFound == 0:
        num1 = random.randrange(self.Board.size)
        boardNum = self.Board.move(num1)
        if boardNum != 0:
            highestNumFound = boardNum
        print(highestNumFound, num1)
    while True:
        boardNum2 = self.Board.move(num1+1)
        boardNum3 = self.Board.move(num1-1)
        if num1 == 0:
            if boardNum2 > highestNumFound:
                highestNumFound = boardNum2
                num1 += 1
            else:
                return num1
        elif num1 == self.Board.size - 1:
            if boardNum3 > highestNumFound:
                highestNumFound = boardNum3
                num1 -= 1
            else:
                return num1
        else:
            # if highestNumFound is greater than left and right nums, return num1
            # if highestNumFound is greater than left but not right num, set highestNumFound to left num and num1 += 1
            # if highestNumFound is greater than right but not left num, set highestNumFound to right num and num1 -= 1
            return num1