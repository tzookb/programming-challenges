from typing import Counter, List, Optional

class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        max_sum = 0
        for bottom in range(2, len(grid)):
            for right in range(2, len(grid[0])):
                cur_sum = (
                    grid[bottom - 2][right - 2] +
                    grid[bottom - 2][right - 1] +
                    grid[bottom - 2][right] +

                    grid[bottom - 1][right - 1] +

                    grid[bottom][right - 2] +
                    grid[bottom][right - 1] +
                    grid[bottom][right]
                )
                max_sum = max(max_sum, cur_sum)
        return max_sum

grid = [[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]]

s = Solution()
res = s.maxSum(grid)
print(res)