from typing import List

class Solution:
    def recu(self, openers: int, closers: int, cur) -> List[str]:
        if openers + closers == 0:
            return [cur]
        results = []
        if openers > 0:
            results += self.recu(openers - 1, closers, cur + ["("])
        if closers > openers:
            results += self.recu(openers, closers - 1, cur + [")"]) 
        return results

    def generateParenthesis(self, n: int) -> List[str]:
        res = self.recu(n, n, [])
        return list(map(lambda x: "".join(x), res))

s = Solution()
res = s.generateParenthesis(3)
print(res)