from typing import List
import collections

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = collections.Counter()
        sums[0] = 1
        sum = 0
        for num in nums:
            sum += num
            if (sum - k) in sums:
                count += sums[sum - k]
            sums[sum] += 1
        return count

s = Solution()
res = s.subarraySum([1,1,1], 2)
print(res)
