from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        
        cnt = Counter(arr)
        for item in sorted(arr, key = abs):
            if cnt[item] == 0: continue
            if cnt[item * 2] == 0: return False
            cnt[item] -= 1
            cnt[item * 2] -= 1

        return True

s = Solution()
res = s.canReorderDoubled([4,8,2,1])
print(res)