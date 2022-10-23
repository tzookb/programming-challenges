from heapq import heappop, heappush
from typing import Counter, Dict, List, Optional


class Solution:
    def reorganizeString(self, S: str) -> str:
        items = []
        cnt = Counter(list(S))
        for c in cnt:
            heappush(items, (-cnt[c], c))
        
        arranged = [None]
        left = None
        while items:
            times, highest = heappop(items)
            times = -times
            if arranged[-1] == highest:
                return ""
            arranged.append(highest)

            if left:
                heappush(items, left)
                left = None
            
            if times > 1:
                left = (-(times - 1), highest)
            
        
        if left:
            if left[0] > 1:
                return ""
            if left[1] == arranged[-1]:
                return ""
            arranged.append(left[1])
        
        arranged.pop(0)
        return "".join(arranged)

s = Solution()
res = s.reorganizeString("aaab")
print(res)