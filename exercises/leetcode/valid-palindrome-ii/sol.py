class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            a = s[i]
            b = s[j]
            if a != b:
                left = s[i:j+1]
                return (
                    self.isPalindrome(left[1:])
                    or
                    self.isPalindrome(left[0:-1])
                )
            i += 1
            j -= 1
        return True

s = Solution()
s.validPalindrome('abecddcba')