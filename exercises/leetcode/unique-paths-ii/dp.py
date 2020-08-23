from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dp = [1] * len(obstacleGrid[0])
        for j in range(1, len(obstacleGrid)):
            for i in range(1, len(obstacleGrid[0])):
                nextVal = 0
                if obstacleGrid[j][i] == 1:
                    nextVal = -1
                else:
                    if dp[i] != -1:
                        nextVal += dp[i]
                    if dp[i - 1] != -1:
                        nextVal += dp[i - 1]
                dp[i] = nextVal

        if len(dp) == 1 and obstacleGrid[0][0] == 1:
            return 0
        if obstacleGrid[-1][-1] == 1:
            return 0
        return dp[-1]
