from heapq import heappop, heappush
from typing import Counter, Dict, List, Optional

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        pq = [(grid[0][0], 0, 0)]
        max_level = float("-inf")
        seen = {(0, 0)}

        def addItemIfInBound(row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if (row, col) in seen:
                return
            heappush(pq, (grid[row][col], row, col))

        def isDone(row, col):
            return (row == len(grid) - 1 and col == len(grid[0]) - 1)

        while pq:
            val, row, col = heappop(pq)
            max_level = max(max_level, val)
            if isDone(row, col):
                return max_level

            seen.add((row, col))
            addItemIfInBound(row - 1, col)
            addItemIfInBound(row + 1, col)
            addItemIfInBound(row, col - 1)
            addItemIfInBound(row, col + 1)

grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]

s = Solution()
res = s.swimInWater(grid)
print(res)