from typing import List

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last_idx = None
        size = len(number)
        for idx in range(len(number)):
            cur = number[idx]
            if cur != digit:
                continue
            last_idx = idx
            if idx == size - 1:
                break
            after = number[idx + 1]
            if int(after) > int(cur):
                break

        return number[0:last_idx] + number[last_idx + 1:]



s = Solution()
res = s.removeDigit("12313", "3")
print(res)
