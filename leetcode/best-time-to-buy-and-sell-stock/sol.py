from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        potentialProfit = 0
        minPrice = float('inf')

        for pr in prices:
            if pr < minPrice:
                minPrice = pr
            elif pr - minPrice > potentialProfit:
                potentialProfit = pr - minPrice

        return potentialProfit

s = Solution()
res = s.maxProfit([7,1,5,3,6,4])

print(res)