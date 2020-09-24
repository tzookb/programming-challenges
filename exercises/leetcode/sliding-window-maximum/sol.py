from typing import List
import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_till = []
        cur_max = float("-inf")

        for num in nums:
            cur_max = max(cur_max, num)
            max_till.append(cur_max)
        
        i = k - 1
        while i < len(nums):
            res_max = max_till[i]
            res.append(res_max)
            i += 1
            
        return res
    
[1, -1]
[1,  1]
[1, -1]

[1,3,-1,-3,5,3,6,7]
[1,3,3,3,5,5,6,7]
[]
s = Solution()
res = s.maxSlidingWindow(
    [1,3,-1,-3,5,3,6,7], 3
    # [1,3,-1,-3, 2], 3
)
print(res)