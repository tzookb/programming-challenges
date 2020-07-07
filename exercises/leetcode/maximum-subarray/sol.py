from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxV = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i-1] > nums[i]:
                nums[i] = nums[i] + nums[i-1]
            if nums[i] > maxV:
                maxV = nums[i]
        return maxV



nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
s = Solution()
res = s.maxSubArray(nums)
# res = s.calcNext("1211")
print(res)