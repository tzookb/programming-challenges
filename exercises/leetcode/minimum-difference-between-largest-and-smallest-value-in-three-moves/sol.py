class Solution:
    def minDifference(self, nums: list[int]) -> int:
        if len(nums) < 5:
            return 0

        nums.sort()
        diff = float("inf")
        for i in range(4):
            diff = min(diff, nums[len(nums) - 4 + i] - nums[i])
        return diff
