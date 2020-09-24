from typing import List
from collections import Counter
class Solution:

    def get_chars_counter(self, s: str):
        cnt = Counter()
        for c in s:
            cnt[c] += 1 
        return cnt

    def check_counts(self, c1, c2) -> bool:
        return c1 == c2
    
    def findAnagrams(self, s: str, p: str) -> List[int]:
        solutions = []
        target_len = len(p)
        src_len = len(s)
        if target_len > src_len:
            return solutions
        if target_len == 0:
            return solutions

        target_cnt = self.get_chars_counter(p)
        source_cnt = self.get_chars_counter(s[0:target_len])

        if self.check_counts(target_cnt, source_cnt):
            solutions.append(0)

        for i in range(target_len, src_len):
            to_remove = s[i - target_len]
            to_add = s[i]
            source_cnt[to_remove] -= 1
            if source_cnt[to_remove] == 0:
                del source_cnt[to_remove]
            
            source_cnt[to_add] += 1

            if to_add in target_cnt:
                if self.check_counts(target_cnt, source_cnt):
                    solutions.append(i - target_len + 1)

        return solutions

s = Solution()
res = s.findAnagrams("abab", "") 
print(res)