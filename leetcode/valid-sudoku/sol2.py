from collections import Counter
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        li2 = []
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c != '.':
                    for x in ((c, i), (j, c), ((int)(i/3),(int)(j/3), c)):
                        li2.append(x)
        ci = Counter(li2)
        if ci.most_common(1): #skip when empty board
            if 1 != ci.most_common(1)[0][1] :
                return False
        return True