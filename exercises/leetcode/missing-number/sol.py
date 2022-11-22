from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) // 2
        cur_total = sum(nums)
        diff = total - cur_total
        return diff
