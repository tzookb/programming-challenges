class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if len(s) % 2 == 1:
            left = right = len(s) // 2
        else:
            right = int(len(s) / 2)
            left = right - 1

        while not self.checkPalToEnd(s, left, right) and left >= 0:
            if left == right:
                left -= 1
            else:
                right = left

        connect = s[right:]
        connect = connect[left+1:]
        connect = connect[::-1]
        
        return connect + s

    def checkPalToEnd(self, s: str, left, right) -> bool:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return left == -1

        
        