class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        i = lastPos

        while i >= 0:
            curStepSize = nums[i]
            if i + curStepSize >= lastPos:
                lastPos = i
            i -= 1

        return lastPos == 0