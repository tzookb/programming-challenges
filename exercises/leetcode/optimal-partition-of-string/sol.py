from typing import List, Counter

class Solution:
    def partitionString(self, s: str) -> int:
        cur = {}
        partitions = 0
        for c in s:
            if c in cur:
                cur = {}
                cur[c] = True
                partitions += 1
                continue
            cur[c] = True

        if cur:
            partitions += 1
        return partitions 
