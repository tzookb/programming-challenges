from typing import List
class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        count = 0
        left = 0
        while left < len(s):
            right = left
            while right < len(s) and int(s[left:right + 1]) <= k:
                right += 1

            if left == right:
                return -1

            left = right
            count += 1
        return count


s = Solution()
res = s.minimumPartition("165462", 60)
# res = s.minimumPartition("238182", 5)
print(res)