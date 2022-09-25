from typing import Counter, List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [0] * len(obstacleGrid[0])
        dp[0] = 1

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                cur = obstacleGrid[row][col]
                if cur == 1:
                    dp[col] = 0
                    continue
                above = dp[col]
                left = 0 if col == 0 else dp[col - 1]
                dp[col] = above + left
            print(dp)
        return dp[-1]
        

grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
# [1,1,1],
# [1,0,1],
# [1,1,2]
# grid = [[0,1],[0,0]]
# grid = [[0,0],[0,1]]
# grid = [[0]]
# grid = [[0,0]]
s = Solution()
res = s.uniquePathsWithObstacles(grid)
print(res)