from typing import List
import math
from heapq import heappush, heappop

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = []
        for i in range(len(nums)):
            heappush(heap, -nums[i])
        
        summed = 0
        for i in range(k):
            popped = heappop(heap)
            
            popped = -popped
            summed += popped
            heappush(heap, -math.ceil(popped/3))
        
        return summed

s = Solution()
res = s.maxKelements([1,10,3,3,3], 3)
print(res)
