from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = Counter()
        for num in nums:
            counts[num] += 1
        cur = 0
        for i in range(len(nums)):
            if counts[0]:
                counts[0] -= 1
                nums[i] = 0
            elif counts[1]:
                counts[1] -= 1
                nums[i] = 1
            else:
                nums[i] = 2
