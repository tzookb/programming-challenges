from typing import List
from sortedcontainers import SortedList
from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sl = SortedList()
        result = [0]
        sl.add(nums[-1])

        for item in nums[::-1][1:]:
            sl.add(item)
            items_on_left = sl.bisect_left(item)
            result.insert(0, items_on_left)
        
        return result
            

# nums = [5,2,6,1]
nums = [-1, -1]
s = Solution()
res = s.countSmaller(nums)
print(res)