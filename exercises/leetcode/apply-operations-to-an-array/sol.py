from typing import Counter, Dict, List, Optional

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                continue
            nums[i] *= 2
            nums[i + 1] = 0
        
        next_pos = 0
        curidx = 0
        counted_zeros = 0
        while curidx < len(nums):
            val = nums[curidx]
            curidx += 1

            if val == 0:
                counted_zeros += 1
                continue

            nums[next_pos] = val
            next_pos += 1

        while counted_zeros > 0:
            nums[len(nums) - counted_zeros] = 0
            counted_zeros -= 1

        return nums


s = Solution()
sol = s.applyOperations([1,2,2,1,1,0])
sol = s.applyOperations([0, 1])
print(sol)