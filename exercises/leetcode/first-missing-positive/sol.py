from typing import Counter, List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # zero negative numbers or too big numbers
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
            if nums[i] > len(nums):
                nums[i] = 0
        
        # mark found numbers as negatives by positions
        for i in range(len(nums)):
            cur = nums[i]
            if cur == 0:
                continue
            real_pos = abs(cur) - 1
            if nums[real_pos] > 0:
                nums[real_pos] *= -1
            elif nums[real_pos] == 0:
                nums[real_pos] = -(real_pos + 1)
            nums[real_pos] = nums[real_pos] if nums[real_pos] < 0 else -nums[real_pos]

        # find the missing one
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1

        return len(nums) + 1

s = Solution()
# res = s.firstMissingPositive([3,4,-1,1])
# res = s.firstMissingPositive([1,2,3,4])
# res = s.firstMissingPositive([1,2,0])
# res = s.firstMissingPositive([0,1,2,0,0])
res = s.firstMissingPositive([2,2])
print(res)
