from typing import Counter, Dict, List, Optional

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        for idx in range(len(pref) - 1, 0, -1):
            pref[idx] ^= pref[idx - 1] 
            
        return pref




pref = [5,2,0,3,1]
s = Solution()
res = s.findArray(pref)
print(res)