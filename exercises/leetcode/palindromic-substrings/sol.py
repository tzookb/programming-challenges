from typing import List

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        for i, _ in enumerate(s):
            result += self.countPalindromsFromMiddle(s, i, i)
            result += self.countPalindromsFromMiddle(s, i, i + 1)
        
        return result

    def countPalindromsFromMiddle(self, s: str, left, right) -> int:
        result = 0

        while left >= 0 and right < len(s) and s[left] == s[right]:
            result += 1
            right += 1
            left -= 1

        return result

s = Solution()
res = s.countSubstrings("abba")
print(res)