from typing import List
import collections

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0 or s == "":
            return 0
        if len(s) == 1:
            return 1
        values = collections.Counter()
        maxLen = 0
        start = 0
        end = 1
        values[s[start]] += 1
        values[s[end]] += 1

        while start <= end and end < len(s):            
            uniqueKeysCnt = len(values)
            subLen = end - start + 1
            if uniqueKeysCnt > k:
                values[s[start]] -= 1
                if values[s[start]] == 0:
                    del values[s[start]]
                start += 1
            else:
                if subLen > maxLen:
                    maxLen = subLen
                end += 1
                if end >= len(s):
                    break
                values[s[end]] += 1

        return maxLen

s = Solution()
res = s.lengthOfLongestSubstringKDistinct("bacc", 2)
print(res)
