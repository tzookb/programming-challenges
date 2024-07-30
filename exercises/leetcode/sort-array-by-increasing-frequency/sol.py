from functools import cmp_to_key
from typing import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        def compare(i1, i2):
            print(counts, i1, i2)
            if counts[i1] == counts[i2]:
                return i2 - i1
            return counts[i1] - counts[i2]

        nums = sorted(nums, key=cmp_to_key(compare))
        return nums