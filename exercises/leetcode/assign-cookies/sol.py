from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        cookieIdx = childIdx = 0
        while childIdx < len(g) and cookieIdx < len(s):
            if g[childIdx] <= s[cookieIdx]:
                cookieIdx += 1
            childIdx += 1
        return cookieIdx

children = [1,2]
cookies = [1,2,3]
s = Solution()
res = s.findContentChildren(children, cookies)
print(res)