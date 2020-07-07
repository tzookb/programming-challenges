from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i
        

# nums = [3, 3]
# val = 3
# nums = [1]
# val = 1
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [3,2,2,3] 
# val = 3
s = Solution()
s.removeElement(nums, val)