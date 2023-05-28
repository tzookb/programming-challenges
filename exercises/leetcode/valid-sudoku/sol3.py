from typing import List, Optional

class Solution:
    SIZE = 9

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        squares = [{} for _ in range(9)]
        
        for row in range(self.SIZE):
            for col in range(self.SIZE):
                item = board[row][col]
                if item == ".":
                    continue
                
                actual_pos = int(item) - 1
                square_pos = self.getSquareByPosition(row, col) - 1

                if actual_pos in rows[row]:
                    return False
                if actual_pos in cols[col]:
                    return False
                if actual_pos in squares[square_pos]:
                    return False
                
                rows[row][actual_pos] = True
                cols[col][actual_pos] = True
                squares[square_pos][actual_pos] = True
        return True
        

    def getSquareByPosition(self, row: int, col: int) -> int:
        mult = row // 3
        left_sqaure_pos = 3 * mult + 1

        horizontal = col // 3

        square = left_sqaure_pos + horizontal
        return square

board = [
    ["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
board = [
    ["8","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
]
s = Solution()
res = s.isValidSudoku(board)
print(res)
