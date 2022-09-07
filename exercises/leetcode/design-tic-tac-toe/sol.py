from typing import List

def isNegDiag(row, col):
    return row == col

def isPosDiag(row, col, n):
    return n - 1 - row == col

def getWinner(num):
    return 1 if num > 0 else 2
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.pos_diag = 0
        self.neg_diag = 0

    def move(self, row: int, col: int, player: int) -> int:
        action = 1 if player == 1 else -1
        self.rows[row] += action
        self.cols[col] += action
        if isNegDiag(row, col):
            self.neg_diag += action
        if isPosDiag(row, col, self.n):
            self.pos_diag += action
        
        if abs(self.rows[row]) == self.n:
            return getWinner(self.rows[row])
        if abs(self.cols[col]) == self.n:
            return getWinner(self.cols[col])
        if abs(self.pos_diag) == self.n:
            return getWinner(self.pos_diag)
        if abs(self.neg_diag) == self.n:
            return getWinner(self.neg_diag)
        
        return 0