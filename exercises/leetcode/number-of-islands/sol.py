from typing import List

class Solution:
    def exploreIsland(self, grid: List[List[str]], row: int, col: int) -> int:
        grid[row][col] = 0
        rowLen = len(grid)
        colLen = len(grid[0])
        if row > 0 and grid[row-1][col] == "1": # up
            grid = self.exploreIsland(grid, row - 1, col)
        if col > 0 and grid[row][col-1] == "1": # left
            grid = self.exploreIsland(grid, row, col - 1)
        if col < colLen-1 and grid[row][col+1] == "1": # right
            grid = self.exploreIsland(grid, row, col + 1)
        if row < rowLen-1 and grid[row+1][col] == "1": # bottom
            grid = self.exploreIsland(grid, row+1, col)
        return grid






    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for row, rowV in enumerate(grid):
            for col, colV in enumerate(rowV):
                if grid[row][col] == "1":
                    grid = self.exploreIsland(grid, row, col)
                    count += 1
        return count




first = [
    [1,1,1,1,0],
    [1,1,0,1,0],
    [1,1,0,0,0],
    [0,0,0,0,0],
]
sol = Solution()
res = sol.numIslands(first)
# res = sol.exploreIsland(first, 0, 0)
# print(res)