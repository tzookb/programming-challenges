from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            cur = nums[i]
            if cur <= 0:
                i += 1
                continue
            if cur > len(nums):
                i += 1
                continue
            if cur == i + 1:
                i += 1
                continue
            if cur == nums[cur - 1]:
                i += 1
                continue
            nums[i], nums[cur - 1] = nums[cur - 1], nums[i]
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1
            

items = [1,2,0]
s = Solution()
res = s.firstMissingPositive(items)
print(res)