from typing import List, Optional
from heapq import heappush, heappop

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        end = (len(grid[0]) - 1, len(grid) - 1)
        visited = {}
        
        def isOutOfBounds(pos):
            if pos[0] >= len(grid[0]) or pos[0] < 0:
                return True
            if pos[1] >= len(grid) or pos[1] < 0:
                return True
            return False

        shouldBreak = lambda pos: grid[pos[1]][pos[0]] == 1

        locations = [(0, 0, 0)]
        while locations:
            shortest = heappop(locations)
            breaks = shortest[0]
            position = (shortest[1], shortest[2])
            if position in visited:
                continue
            visited[position] = True

            if isOutOfBounds(position):
                continue
            if position == end:
                return breaks

            if shouldBreak(position):
                breaks += 1

            heappush(locations, (breaks, position[0] + 1, position[1]))
            heappush(locations, (breaks, position[0], position[1] + 1))
            heappush(locations, (breaks, position[0] - 1, position[1]))
            heappush(locations, (breaks, position[0], position[1] - 1))

        return -1



grid = [[0,1,1],[1,1,0],[1,1,0]] # 2
# grid = [[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]] # 0
s = Solution()
res = s.minimumObstacles(grid)
print(res)