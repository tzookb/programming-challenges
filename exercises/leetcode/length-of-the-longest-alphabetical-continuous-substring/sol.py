from typing import Counter, List
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        prev = 0
        cur_len = 0
        max_len = 0
        for c in s:
            asci = ord(c)
            if asci == prev + 1:
                cur_len += 1
            else:
                max_len = max(max_len, cur_len)
                cur_len = 1
            prev = asci
        
        max_len = max(max_len, cur_len)
        return max_len