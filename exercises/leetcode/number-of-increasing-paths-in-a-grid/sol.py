from typing import Counter, List

class Solution:
    modu = 10**9 + 7

    def countPaths(self, grid: List[List[int]]) -> int:
        memo = {}
        count = 0

        def dfs(row, col, prev):
            if row < 0 or row >= len(grid):
                return 0
            if col < 0 or col >= len(grid[0]):
                return 0
            cur = grid[row][col]
            if prev >= cur:
                return 0
            key = (row, col)
            if key in memo:
                return memo[key]
            count = 1
            count += dfs(row - 1, col, cur)
            count += dfs(row + 1, col, cur)
            count += dfs(row, col - 1, cur)
            count += dfs(row, col + 1, cur)
            memo[key] = count % self.modu
            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                res = dfs(row, col, float("-inf"))
                count += res
                count = count % self.modu

        return count

# grid = [[1,1],[3,4]]
grid = [[1],[2]]
s = Solution()
res = s.countPaths(grid)
print(res)