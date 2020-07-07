from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = 0
        while idx < len(nums):
            cur = nums[idx]
            if target <= cur:
                return idx
            idx += 1
        return idx
        

nums = [1, 3, 5, 6]
target = 0
s = Solution()
res = s.searchInsert(nums, target)
print(res)