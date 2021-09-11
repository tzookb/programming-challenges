from typing import List

class Solution:
    
    def reverseWords(self, s: str) -> str:
        words = list(map(self.reverseString, s.split(" ")))
        return " ".join(words)

    def reverseString(self, str) -> None:
        s = list(str)
        l = len(s)
        half = l // 2
        for i in range(half):
            end = l - 1 - i
            s[i], s[end] = s[end], s[i]
        return "".join(s)
