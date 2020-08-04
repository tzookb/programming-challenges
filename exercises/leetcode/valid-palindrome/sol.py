class Solution:
    def isPalindrome(self, s: str) -> bool:
        lowered = s.lower()
        def onlyChars(c):
            ascVal = ord(c)
            return 122 >= ascVal >= 97 or 57 >= ascVal >= 48
        final = "".join(list(filter(onlyChars, list(lowered))))
        return final == final[::-1]

s = Solution()
res = s.isPalindrome("race a car")
print(res)