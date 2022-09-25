from typing import Counter, List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0 for x in range(len(obstacleGrid[0]))] for y in range(len(obstacleGrid))] 

        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                cur = obstacleGrid[row][col]
                if row == 0 and col == 0:
                    dp[row][col] = 1
                    continue
                if cur == 1:
                    dp[row][col] = 0
                    continue
                
                above = 0 if row == 0 else dp[row - 1][col]
                left = 0 if col == 0 else dp[row][col - 1]
                dp[row][col] = above + left
        return dp[-1][-1]