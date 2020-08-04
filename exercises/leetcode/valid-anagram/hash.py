from typing import List
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic = collections.Counter()

        for i in range(len(s)):
            dic[s[i]] += 1
            dic[t[i]] -= 1
        
        for key in dic:
            if dic[key] != 0:
                return False
        return True

s = Solution()
res = s.isAnagram('asd', 'dsa')
print(res)
