import heapq
from typing import Counter, List, Optional

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: -x, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            big1 = -heapq.heappop(stones)
            big2 = -heapq.heappop(stones)
            if big1 == big2:
                continue
            left_stone = big1 - big2
            heapq.heappush(stones, -left_stone)
        return 0 if not stones else -stones[0]

stones = [2,7,4,1,8,1]
s = Solution()
res = s.lastStoneWeight(stones)
print(res)