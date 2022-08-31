from typing import List, Counter
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
            prev = s[i - 1]
            c = s[i]
            if prev == c:
                groups[-1] += 1
            else:
                groups.append(1)
        
        total = 0
        for i in range(1, len(groups)):
            prev = groups[i - 1]
            cur = groups[i]
            total += min(prev, cur)
        
        return total

s = Solution()
res = s.countBinarySubstrings("00110011")
print(res)
