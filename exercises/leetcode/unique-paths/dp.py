class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for j in range(1, n):
            for i in range(1, m):
                dp[i] = dp[i] + dp[i-1] 
        return dp[-1]

s = Solution()
res = s.uniquePaths(7, 3)
print(res)