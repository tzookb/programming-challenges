from typing import Counter, List, Optional
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        raw = list(filter(lambda x: x != "-", s))
        groups = []
        group = []
        while raw:
            cur = raw.pop()
            cur = cur.capitalize()
            if len(group) == k:
                groups.append(group)
                group = []
            group.insert(0, cur)
        if group:
            groups.append(group)
        
        groups = groups[::-1]
        groups = ["".join(g) for g in groups]
        return "-".join(groups)

s = Solution()
res = s.licenseKeyFormatting("5F3Z-2e-9-w", 4)
# res = s.licenseKeyFormatting("2-5g-3-J", 2)
print(res)