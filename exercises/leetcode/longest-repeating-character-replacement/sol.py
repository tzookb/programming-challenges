from typing import Counter, List, Optional

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = [0] * 26

        left = right = longest = 0

        getLetterPos = lambda c: ord(c) - ord("A")

        def isGood():
            total = sum(count)
            maxed = max(count)
            return total - maxed <= k

        while right < len(s):
            add = getLetterPos(s[right])
            
            count[add] += 1
            while not isGood():
                rm = getLetterPos(s[left])
                count[rm] -= 1
                left += 1

            longest = max(longest, right - left + 1)
            right += 1

        return longest

s = Solution()
res = s.characterReplacement("ABAB", 2) # 4
res = s.characterReplacement("AABABBA", 1) # 4
print(res)