
class Solution:
    def firstUniqChar(self, s: str) -> int:
        found = {}
        for c in s:
            if c not in found:
                found[c] = 0
            found[c] += 1

        for idx, c in enumerate(s):
            if found[c] == 1:
                return idx

        return -1
                

s = Solution()
res = s.firstUniqChar("aadadaad")
print(res)