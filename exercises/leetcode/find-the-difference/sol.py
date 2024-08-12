from typing import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs = Counter(s)
        ct = Counter(t)
        # print(cs, ct)
        for ks in cs:
            ct[ks] -= cs[ks]
            if ct[ks] == 0:
                del ct[ks]
        
        return list(ct.keys())[0]
        