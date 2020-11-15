from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        leftEnd = -1
        righttEnd = len(matrix[0])
        topEnd = -1
        bottomEnd = len(matrix)
        cur = (0, 0)
        count = 0
        needed = matrix * matrix[0]
        spiral = []
        movement = 'r'

        def move(pos):
            moves = {
                "r": (0, 1),
                "l": (0, -1),
                "u": (-1, 0),
                "d": (1, 0),
            }
            return (pos[0] + moves[pos][0], pos[1] + moves[pos][1])
        
        def isInLimits(pos):
            return (
                leftEnd < pos[0] < righttEnd or
                topEnd < pos[1] < bottomEnd
            )

        def getNext(cur):
            nextPos = move(cur)
            if isInLimits(nextPos):
                return nextPos
            

        def getVal(pos):
            return matrix[pos(1)][pos[0]]

        while count < needed:
            spiral.append(getVal(cur))
            count += 1
            cur = getNext(cur)

x = (0,0)
y = (1,2)
print(x + y)