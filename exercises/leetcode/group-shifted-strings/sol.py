from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        shifts = {}
        for cur in strings:
            initial = self.getInitialShift(cur)
            if initial not in shifts:
                shifts[initial] = []
            shifts[initial].append(cur)

        return list(shifts.values())

    def getInitialShift(self, string: str) -> str:
        if string == "":
            return ""
        parts = list(string)
        
        first = parts[0]
        diff = ord(first) - ord("a")
        
        if not diff:
            return string
        
        for i in range(len(parts)):
            pos = ord(parts[i])
            first = ord("a")
            cur_diff = pos - first
            if diff <= cur_diff:
                parts[i] = chr(pos - diff)
                continue

            from_top = diff - cur_diff

            parts[i] = chr(ord("z") + 1 - from_top)
        
        return "".join(parts)



s = Solution()
res = s.groupStrings(["abc","bcd","acef","xyz","az","ba","a","z"])
print(res)
