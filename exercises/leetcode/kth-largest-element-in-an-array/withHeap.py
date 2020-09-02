from typing import List
from heapq import heappop, heappush, heapify 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        heap = [] 
        heapify(heap) 
        for num in nums:
            heappush(heap, -1 * num) 
        
        for _ in range(k):
            val = heappop(heap) 

        return -1 * val



s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
res = s.findKthLargest(nums, k)
print(res)