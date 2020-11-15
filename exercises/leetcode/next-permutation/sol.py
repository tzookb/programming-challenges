from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # find the minimun number which could be replaced
        replace_index = replace_with_index = -1
        lastIndex = len(nums)-1
        for i in range(lastIndex, 0, -1):
            if nums[i] > nums[i-1]:
                replace_index = i-1
                break
        if replace_index == -1:
            nums.sort()
            return
        
        replace_val = nums[replace_index]

        # find replace with idx
        replaceWithIdx = replace_index + 1

        while replaceWithIdx <= lastIndex:
            cur = nums[replaceWithIdx]
            if replace_val >= cur:
                replaceWithIdx -= 1
                break
            replaceWithIdx += 1
        
        replaceWithIdx = min(lastIndex, replaceWithIdx)
        
        nums[replace_index], nums[replaceWithIdx] = nums[replaceWithIdx], nums[replace_index]

        nums[replace_index+1:] = sorted(nums[replace_index+1:])


p = [1,5,1]
s = Solution()
s.nextPermutation(p)
print(p)