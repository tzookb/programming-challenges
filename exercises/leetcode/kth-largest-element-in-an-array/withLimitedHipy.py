from typing import List
from heapq import heappop, heappush, heapify

class OwnHeap:
    def __init__(self, limit, type="min"):
        self.heap = []
        self.limit = limit
        self.type = type
        heapify(self.heap)

    def multWithType(self, val):
        mult = 1 if self.type == "min" else -1
        return val * mult

    def add(self, val):
        heappush(self.heap, self.multWithType(val)) 
        if len(self.heap) > self.limit:
            self.pop()

    def pop(self):
        return self.multWithType(heappop(self.heap))

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        count = 0
        heap = OwnHeap(k)

        for num in nums:
            heap.add(num)

        return heap.pop()

s = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
res = s.findKthLargest(nums, k)
print(res)