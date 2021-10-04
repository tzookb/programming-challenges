from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        size = len(nums)
        more_than = size // 2
        for num in c:
            count = c[num]
            if count > more_than:
                return num
        raise "error"

s = Solution()
res = s.majorityElement([3,2,3])
print(res)