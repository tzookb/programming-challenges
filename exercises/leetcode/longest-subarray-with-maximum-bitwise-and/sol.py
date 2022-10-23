from typing import Counter, List, Optional

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxval = max(nums)
        maxcount = 0 
        curcount = 0
        for item in nums:
            if item == maxval:
                curcount += 1
            else:
                curcount = 0
            maxcount = max(maxcount, curcount)
        return maxcount

s = Solution()
res = s.longestSubarray([1,2,3,3,2,2])
res = s.longestSubarray([1,2,3,4])
print(res)