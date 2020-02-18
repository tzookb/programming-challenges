from typing import List

class Solution:

    def getSquareByXY(self, x, y):
        if x >= 0 and x<=2:
            if y >= 0 and y<=2:
                return "0"
            elif y >= 3 and y<=5:
                return "3"
            else:
                return "6"
        elif x >= 3 and x<=5:
            if y >= 0 and y<=2:
                return "1"
            elif y >= 3 and y<=5:
                return "4"
            else:
                return "7"
        else:
            if y >= 0 and y<=2:
                return "2"
            elif y >= 3 and y<=5:
                return "5"
            else:
                return "8"

    def getPresetMap(self):
        return {
            "0": {},
            "1": {},
            "2": {},
            "3": {},
            "4": {},
            "5": {},
            "6": {},
            "7": {},
            "8": {},
        }

    
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        self.rows = self.getPresetMap()
        self.columns = self.getPresetMap()
        self.squares = self.getPresetMap()

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                if val == '.':
                    continue
                if str(val) not in self.rows[str(y)]:
                    self.rows[str(y)][str(val)] = 0
                self.rows[str(y)][str(val)] += 1
                if self.rows[str(y)][str(val)] > 1:
                    return False
                
                if str(val) not in self.columns[str(x)]:
                    self.columns[str(x)][str(val)] = 0
                self.columns[str(x)][str(val)] += 1
                if self.columns[str(x)][str(val)] > 1:
                    print('yy')
                    return False

                if str(val) not in self.squares[self.getSquareByXY(x, y)]:
                    self.squares[self.getSquareByXY(x, y)][str(val)] = 0
                self.squares[self.getSquareByXY(x, y)][str(val)] += 1
                if self.squares[self.getSquareByXY(x, y)][str(val)] > 1:
                    print('z')
                    return False
        return True

s = Solution()
q = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(s.isValidSudoku(q))