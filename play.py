from typing import List, Optional

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        counts = [0] * 26
        left = right = 0
        max_size = -1

        def isValid():
            for count in counts:
                if count == 0:
                    continue
                if count < k:
                    return False
            return True

        while right < len(s):
            cur = s[right]
            cur_pos = ord(cur) - ord("a")
            counts[cur_pos] += 1
            if counts[cur_pos] < k:
                max_size = max(max_size, right - left + 1)
                right += 1
                continue

            print("isvalid", s[left:right+1])
            if isValid():
                max_size = max(max_size, right - left + 1)
                right += 1
                continue

            while not isValid() and left <= right:
                remove = s[left]
                remove = ord(remove) - ord("a")
                counts[remove] -= 1
                left += 1

            right += 1

        return max_size

s = Solution()
res = s.longestSubstring("ababbc", 2)
print(res)