from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        for i in range(len(prices) - 1):
            cur = prices[i]
            nextV = prices[i+1]
            if nextV > cur:
                total += nextV - cur
        return total
