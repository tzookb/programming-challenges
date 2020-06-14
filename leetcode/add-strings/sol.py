import math

class Solution:
    def get_val(self, str: str, idx: int) -> int:
        try:
            return ord(str[::-1][idx]) - 48
        except IndexError:
            return 0

    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        length = max(len(num1), len(num2))
        i = 0
        remainder = 0
        while i < length:
            v1 = self.get_val(num1, i)
            v2 = self.get_val(num2, i)
            total = v1 + v2 + remainder
            remainder = math.floor(total / 10)
            result.insert(0, str(total % 10))
            i += 1
        if remainder:
            result.insert(0, str(remainder))
        return "".join(result)