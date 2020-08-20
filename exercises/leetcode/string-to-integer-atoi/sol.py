from typing import List

class Solution:
    def myAtoi(self, str: str) -> int:
        stripped = str.strip()
        if len(stripped) == 0:
            return 0
        maxii = 2147483647
        minii = -2147483648
        sign = 1
        if stripped[0] == "-":
            sign = -1
            stripped = stripped[1:]
        elif stripped[0] == "+":
            sign = 1
            stripped = stripped[1:]
        total = 0
        for char in stripped:
            if 57 < ord(char) or ord(char) < 48:
                break
            total = total*10 + int(char)

        final = sign*total
        return  min(max(minii, final), maxii)

s = Solution()
res = s.myAtoi("-91283472332")
print(res)
