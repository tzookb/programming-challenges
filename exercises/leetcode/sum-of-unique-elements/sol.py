from typing import Counter, Dict

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        total = 0
        for num in cnt:
            count = cnt[num]
            if count > 1:
                continue
            total += num
        return total