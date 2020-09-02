from typing import List
from heapq import heappop, heappush, heapify

class MaxHeap:
    def __init__(self):
        self.heap = []
        heapify(self.heap)

    def add(self, val):
        heappush(self.heap, -1 * val) 

    def pop(self):
         return -1 * heappop(self.heap) 

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        heap = MaxHeap()
        
        for num in nums:
            heap.add(num)
        
        for _ in range(k):
            val = heap.pop()

        return val



s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
res = s.findKthLargest(nums, k)
print(res)