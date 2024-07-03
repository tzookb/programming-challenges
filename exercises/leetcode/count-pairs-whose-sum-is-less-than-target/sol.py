class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        counts = 0
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if nums[i] + nums[j] < target:
                    counts += 1
        return counts
