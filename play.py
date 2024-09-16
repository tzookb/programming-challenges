from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
        self.position = [0, 0]
        self.directions = [(0, 1), (1, 0), (0, -1), (0, -1)]
        self.directionIdx = 0
        self.m = 3
        self.n = 5

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1 for _ in range(n)] for _ in range(m)]

        cur = head
        while cur:
            print(self.position)
            mat[self.position[0]][self.position[1]] = cur.val
            cur = cur.next
            self.moveToNext()
        
        return mat
    
    def isPosOutOfBounds(self):
        if self.position[0] < 0 or self.position[0] >= self.m:
            return True
        if self.position[1] < 0 or self.position[1] >= self.n:
            return True
        return False

    def changeDirection(self):
        self.directionIdx += 1
        if self.directionIdx == 4:
            self.directionIdx = 0

    def moveStepForward(self):
        direction = self.directions[self.directionIdx]
        self.position[0] += direction[0]
        self.position[1] += direction[1]

    def moveStepBackward(self):
        direction = self.directions[self.directionIdx]
        self.position[0] -= direction[0]
        self.position[1] -= direction[1]

    def moveToNext(self):
        self.moveStepForward()
        if self.isPosOutOfBounds():
            self.moveStepBackward()
            self.changeDirection()
            self.moveStepForward()

s = Solution()
s.position = [2, 0]
s.directionIdx = 0
s.moveToNext()
print(s.position)