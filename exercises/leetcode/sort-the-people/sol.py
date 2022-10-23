from typing import Counter, List, Optional

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = sorted(zip(names, heights), key=lambda x: x[1], reverse=True)
        return list(map(lambda x: x[0], res))

names = ["Alice","Bob","Bob"]
heights = [155,185,150]

s = Solution()
s.sortPeople(names, heights)