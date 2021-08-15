import math

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        med = math.floor(math.median(nums))
        diff = 0

        for num in nums:
            diff += abs(med - num)
        
        return diff
        