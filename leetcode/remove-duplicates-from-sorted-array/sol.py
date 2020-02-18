from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1

arr = [1,1,1,1,1,2,2,2,3]
s = Solution()
r = s.removeDuplicates(arr)
print(arr)
print(r)