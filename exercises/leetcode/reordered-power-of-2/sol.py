from typing import List
from collections import Counter

class Solution:
    def getPossiblePowers(self, size: int) -> List[int]:
        cur_size = 1
        cur = 1
        options = []

        while cur_size <= size:
            if cur_size == size:
                options.append(cur)
            cur *= 2
            cur_size = len(str(cur))
        return options

    def checkIfPossible(self, n1: int, n2: int) -> bool:
        c1 = Counter(list(str(n1)))
        c2 = Counter(list(str(n2)))
        compared = c2 - c1 | c1 - c2
        return len(compared) == 0
        

    def reorderedPowerOf2(self, N: int) -> bool:
        options = self.getPossiblePowers(len(str(N)))
        for option in options:
            if self.checkIfPossible(N, option):
                return True
        return False

s = Solution()
res = s.reorderedPowerOf2(23)
# res = s.checkIfPossible(1112, 1112)
print(res)