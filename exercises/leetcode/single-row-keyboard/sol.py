from typing import Counter, List

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        positions = {}
        for i, c in enumerate(keyboard):
            positions[c] = i
        
        time = 0
        pos = 0
        for c in word:
            new_pos = positions[c]
            diff = abs(new_pos - pos)
            time += diff
            pos = new_pos
        
        return time

keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"

s = Solution()
res = s.calculateTime(keyboard, word)
print(res)