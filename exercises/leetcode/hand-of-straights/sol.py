import heapq
from typing import Counter, List, Optional
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        cnt = Counter(hand)
        items = []
        for key in cnt:
            items.append((key, cnt[key]))
        heapq.heapify(items)

        for_later = []
        last_item = None
        cur_group_size = 0
        while items:
            val, count = heapq.heappop(items)
            if cur_group_size > 0 and val - last_item > 1:
                return False
            last_item = val
            cur_group_size += 1
            
            if count > 1:
                for_later.append((val, count - 1))
            if cur_group_size == groupSize:
                cur_group_size = 0
                last_item = None
                for left_item in for_later:
                    heapq.heappush(items, left_item)
                for_later = []

        return cur_group_size == 0



hand = [8,10,12]
groupSize = 3

s = Solution()
res = s.isNStraightHand(hand, groupSize)
print(res)