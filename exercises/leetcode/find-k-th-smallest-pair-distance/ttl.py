from heapq import heapify, heappop, heappush
from typing import Counter, List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # sort nums
        # create max heap
        # n^2 loop nums to get dist between points
        # if heap is smaller than K, insert and continue
        # if cur_dist >= heap_max, break current num loop
        # else, pop heap and insert new val
        nums.sort()
        heap = []

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                dist = nums[right] - nums[left]
                if len(heap) < k:
                    heappush(heap, -dist)
                    continue
                if dist >= -heap[0]:
                    break
                heappop(heap)
                heappush(heap, -dist)
        
        return -heap[0]

s = Solution()
res = s.smallestDistancePair([1,3,1], 1) # 0
# res = s.smallestDistancePair([1,1,1], 2) # 0
# res = s.smallestDistancePair([1,6,1], 3) # 5
print(res)