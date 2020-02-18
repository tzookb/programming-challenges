class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == ''.join(list(str(x))[::-1])
