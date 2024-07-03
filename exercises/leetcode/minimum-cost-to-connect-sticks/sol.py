from typing import List, Counter
from heapq import heappush, heappop, heapify

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks)
        work = 0
        while len(sticks) > 1:
            min1 = heappop(sticks)
            min2 = heappop(sticks)
            joined = min1 + min2
            work += joined
            heappush(sticks, joined)
        
        return work


s = Solution()
res = s.connectSticks([1,8,3,5])
print(res)