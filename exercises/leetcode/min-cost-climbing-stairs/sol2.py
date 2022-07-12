from typing import Counter, List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) < 3:
            return min(cost)

        dp = [float("inf")] * (len(cost) + 1)
        dp[0] = dp[1] = 0

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])

        return dp[-1]

s = Solution()
costs = [1,100,1,1,1,100,1,1,100,1]
res = s.minCostClimbingStairs(costs)
print(res)