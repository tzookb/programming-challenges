from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        cur = [1]
        rows = []

        for dontcare in range(numRows):
            rows.append(cur)
            print(cur)
            cur = cur + [0]
            for i in range(len(cur) - 1, 0, -1):
                cur[i] += cur[i - 1]
        return rows

s = Solution()
res = s.generate(5)
print(res)
