
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)

        for i in range(1, len(dp)):
            if i not in days:
                dp[i] = dp[i - 1]
                continue
            
            dp[i] = min(
                dp[max(i - 1, 0)] + costs[0],
                dp[max(i - 7, 0)] + costs[1],
                dp[max(i - 30, 0)] + costs[2],
            )
        return dp[-1]


days = [1,4,6,7,8,20]
costs = [2,7,15]
s = Solution()
res = s.mincostTickets(days, costs)
print(res)