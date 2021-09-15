from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = {}

        def dfs(row, col):
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            if grid[row][col] == 0:
                return 0
            key = f"{row}-{col}"
            if key in visited:
                return 0
            visited[key] = True
            return (
                1 +
                dfs(row, col - 1) +
                dfs(row, col + 1) +
                dfs(row - 1, col) +
                dfs(row + 1, col)
            )

        
        max_island = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                key = f"{r}-{c}"
                if key in visited:
                    continue
                if grid[r][c] == 0:
                    continue
                cur_island = dfs(r, c)
                max_island = max(max_island, cur_island)
        
        return max_island


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
s = Solution()
res = s.maxAreaOfIsland(grid)
print(res)