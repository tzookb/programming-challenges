from typing import List
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        total = 0
        oddCounts = 0
        for num in counts:
            if counts[num] % 2 == 0:
                total += counts[num]
                continue
            total += counts[num] - 1
            oddCounts += 1

        if oddCounts > 0:
            total += 1

        return total

s = Solution()
res = s.longestPalindrome("a")
print(res)