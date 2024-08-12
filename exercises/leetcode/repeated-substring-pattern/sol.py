class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        msz = len(s) // 2
        for i in range(1, msz + 1):
            comped = s[i:] + s[0:i]
            if s == comped:
                return s[0:i]

        