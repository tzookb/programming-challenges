class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        cur_cost = costs[0]

        for house_cost in costs[1:]:
            next_cost = [
                min(
                    house_cost[0] + cur_cost[1],
                    house_cost[0] + cur_cost[2]
                ),
                min(
                    house_cost[1] + cur_cost[0],
                    house_cost[1] + cur_cost[2]
                ),
                min(
                    house_cost[2] + cur_cost[0],
                    house_cost[2] + cur_cost[1]
                ),
            ]
            cur_cost = next_cost
        
        return min(cur_cost)