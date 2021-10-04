from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        cur = [1]

        for dontcare in range(rowIndex):
            cur = cur + [0]
            for i in range(len(cur) - 1, 0, -1):
                cur[i] += cur[i - 1]
        return cur