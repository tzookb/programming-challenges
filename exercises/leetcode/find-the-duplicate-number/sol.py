from typing import List, Dict, Tuple
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        low = 1
        high = len(nums) - 1
        duplicate = None
        while low <= high:
            cur = low + (high - low) // 2
            counts = sum([x <= cur for x in nums])
            if counts > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
        
        return duplicate

s = Solution()
res = s.findDuplicate([1,3,4,2,2])

print(res)

