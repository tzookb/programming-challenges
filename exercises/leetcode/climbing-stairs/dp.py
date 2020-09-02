class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1, 2]

        n -= 2
        while n:
            last = len(dp) - 1
            dp.append(dp[last] + dp[last - 1])
            n -= 1
        return dp[-1]

s = Solution()
res = s.climbStairs(3)
print(res)