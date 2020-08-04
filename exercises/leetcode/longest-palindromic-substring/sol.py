class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        if len(s) == 1:
            return s
        maxLen = 0
        maxStr = ''
        for i in range(len(s)-1):
            noMiddle = self.getFromCenter(s, i, i + 1)
            oneMiddle = self.getFromCenter(s, i, i)
            curMaxLen = max(noMiddle, oneMiddle)
            if curMaxLen > maxLen:
                maxLen = curMaxLen
                start = i - (maxLen - 1) // 2;
                end = i + maxLen // 2;
                maxStr = s[start:end+1]
        return maxStr

    def getFromCenter(self, s: str, l: int, r: int) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        l += 1
        r -= 1
        return len(s[l:r+1])

s = Solution()
res = s.longestPalindrome('a')
# res = s.getFromCenter('babad', 1,2)
print(res)