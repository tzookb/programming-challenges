from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        paths = [
            cost[0],
            cost[1]
        ]
        for i in range(2, len(cost)):
            cur_cost = cost[i]
            min_cost = min(
                paths[i-2],
                paths[i-1]
            ) + cur_cost
            paths.append(min_cost)

        return min(paths[-1], paths[-2])

s = Solution()
res = s.minCostClimbingStairs([10, 15, 20])
print(res)