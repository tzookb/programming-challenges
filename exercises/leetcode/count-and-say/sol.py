from typing import List

class Solution:
    def calcNext(self, n: str) -> str:
        count = 0
        prev = -1
        res = []
        for i in range(len(n)):
            cur = n[i]
            if cur == prev:
                count += 1
            else:
                if count:
                    res.append(str(count))
                    res.append(prev)
                count = 1
                prev = cur
        if count:
            res.append(str(count))
            res.append(prev)
        return ''.join(res)

    def countAndSay(self, n: int) -> str:
        val = "1"
        i = 1
        while i < n:
            val = self.calcNext(val)
            i += 1
        return val



s = Solution()
res = s.countAndSay(5)
# res = s.calcNext("1211")
print(res)