class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        for i, v in enumerate(nums):
            if not stack:
                stack.append(i)
            elif nums[stack[-1]] > v:
                stack.append(i)
        
        maxed = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                maxed = max(maxed, i - stack[-1])
                stack.pop()

        return maxed
        