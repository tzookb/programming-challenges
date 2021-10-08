from typing import List

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        items = [i + 1 for i in range(n)]
        pos = 0
        while len(items) > 1:
            pos += k % len(items) - 1
            pos = pos % len(items)
            items = items[0:pos] + items[pos+1:]

        return items[0]

s = Solution()
res = s.findTheWinner(6, 5)
print(res)