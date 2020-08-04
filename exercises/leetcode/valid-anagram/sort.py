from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = list(s)
        sl.sort()
        tl = list(t)
        tl.sort()
        
        return "".join(tl) == "".join(sl)
        
