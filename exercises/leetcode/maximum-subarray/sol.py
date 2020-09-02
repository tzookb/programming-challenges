from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxV = nums[0]
        prevMax = nums[0]
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur + prevMax > cur:
                prevMax = cur + prevMax
            else:
                prevMax = cur
            if prevMax > maxV:
                maxV = prevMax
        return maxV
    


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
res = s.maxSubArray(nums)
# res = s.calcNext("1211")
print(res)