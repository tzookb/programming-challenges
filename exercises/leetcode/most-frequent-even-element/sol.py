from typing import List, Counter

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = list(filter(lambda x: x%2 == 0, nums))
        if not nums:
            return -1
        cnt = Counter(nums)
        max_count = 0
        
        for key in cnt:
            val = cnt[key]
            max_count = max(max_count, val)

        min_val = float("inf")
        for key in cnt:
            val = cnt[key]
            if val == max_count:
                min_val = min(min_val, key)

        return min_val