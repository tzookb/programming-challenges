from typing import List, Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        heap = []

        for key in cnt:
            appears = cnt[key]
            if len(heap) < k:
                heappush(heap, (appears, key))
                continue
            
            if appears > heap[0][0]:
                heappop(heap)
                heappush(heap, (appears, key))
        
        result = []
        while heap:
            val = heappop(heap)
            result.append(val[1])

        return result[::-1]


s = Solution()
res = s.topKFrequent([1,1,1,2,2,3], 2)

print(res)