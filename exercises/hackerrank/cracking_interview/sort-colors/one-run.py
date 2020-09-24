from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zeroIdx = 0
        twoIdx = len(nums) - 1
        cur = 0
        while cur <= twoIdx:
            v = nums[cur]
            if v == 0:
                nums[cur] = nums[zeroIdx]
                nums[zeroIdx] = 0
                zeroIdx += 1
                cur += 1
            elif v == 1:
                cur += 1
            else:
                nums[cur] = nums[twoIdx]
                nums[twoIdx] = 2
                twoIdx -= 1

        
        