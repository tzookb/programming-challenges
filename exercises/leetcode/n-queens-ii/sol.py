
from typing import List, Optional

class Solution:
    def totalNQueens(self, n: int) -> int:
        final = {}
        covered = {
            "rows": {},
            "cols": {},
            "negdig": {},
            "posdig": {},
        }

        def isInCoveredLocation(row, col):
            if row in covered["rows"] and covered["rows"][row] == True:
                return True
            if col in covered["cols"] and covered["cols"][col] == True:
                return True
            difneg = row - col
            difpos = row + col
            if difneg in covered["negdig"] and covered["negdig"][difneg] == True:
                return True
            if difpos in covered["posdig"] and covered["posdig"][difpos] == True:
                return True
            return False

        def createKeyFromPlaceQueens(arr):
            return "_".join(map(lambda x: str(x), arr))

        def backTrack(placedQueens):
            if len(placedQueens) == n:
                key = createKeyFromPlaceQueens(placedQueens)
                final[key] = True
                return
            
            row = len(placedQueens)
            
            for cur_col in range(n):
                if isInCoveredLocation(row, cur_col):
                    continue

                placedQueens.append(cur_col)
                difneg = row - cur_col
                difpos = row + cur_col
                covered["rows"][row] = True
                covered["cols"][cur_col] = True
                covered["negdig"][difneg] = True
                covered["posdig"][difpos] = True
                backTrack(placedQueens)
                covered["rows"][row] = False
                covered["cols"][cur_col] = False
                covered["negdig"][difneg] = False
                covered["posdig"][difpos] = False
                placedQueens.pop()

        backTrack([])

        return len(final)
    
    def buildQueenRepresentation(self, arr):
        def queenPosToStr(pos):
            return "." * pos + "Q" + "." * (len(arr) - pos - 1)
        return list(map(queenPosToStr, arr))
