import collections
from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sums = collections.Counter()
        sums[0] = -1
        curSum = 0
        for i in range(len(nums)):
            print(sums)
            num = nums[i]
            curSum += num
            if k != 0:
                curSum = curSum % k
            if curSum in sums:
                if i - sums[curSum] > 1:
                    return True
            else:
                sums[curSum] = 1
        return False


s = Solution()
res = s.checkSubarraySum([0,1,0,1,0,1], 0)
print(res)