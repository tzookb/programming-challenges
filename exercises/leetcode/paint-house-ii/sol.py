from typing import List, Optional

class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        dp = costs[0]
        for cost in costs[1:]:
            next_dp = []
            for idx, c in enumerate(cost):
                best_prev_cost = min(dp[0:idx] + dp[idx+1:])
                next_dp.append(c + best_prev_cost)
            dp = next_dp

        return min(dp)


s = Solution()
res = s.minCostII([[1,5,3],[2,9,4]])
res = s.minCostII([[1,3],[2,4]])
print(res)