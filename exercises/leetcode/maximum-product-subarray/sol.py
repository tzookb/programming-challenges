import collections
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxTilHere = nums[0]
        minTilHere = nums[0]
        finalMax = nums[0]

        for num in nums[1:]:
            print(maxTilHere, minTilHere, num)
            curMax = max(maxTilHere * num, minTilHere * num, num)
            minTilHere = min(maxTilHere * num, minTilHere * num, num)
            maxTilHere = curMax
            if maxTilHere > finalMax:
                finalMax = maxTilHere
        return finalMax

n = [-4, -3, -2]
s = Solution()
res = s.maxProduct(n)
print(res)
