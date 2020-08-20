from typing import List

class Solution:
    def sum(self, num1: str, num2: str) -> str:
        longer = max(len(num1), len(num2))
        remainder = 0
        total = []

        for i in range(longer):
            v1 = num1[-(i+1)] if i < len(num1) else 0
            v2 = num2[-(i+1)] if i < len(num2) else 0

            subTotal = int(v1) + int(v2) + remainder
            if subTotal > 9:
                remainder = 1
            else:
                remainder = 0
            left = subTotal % 10
            total.insert(0, str(left))
        if remainder:
            total.insert(0, str(remainder))

        return "".join(total)

    def multWithSingle(self, numStr: str, digit: int) -> str:
        if digit == 0:
            return "0"
        remainder = 0
        total = []
        for i in range(len(numStr)):
            v = int(numStr[-(i+1)])
            curMult = v * digit + remainder
            remainder = curMult // 10
            curLeftDigit = curMult % 10
            total.insert(0, str(curLeftDigit))
        if remainder:
            total.insert(0, str(remainder))
        return "".join(total)

    def multiply(self, num1: str, num2: str) -> str:
        total = "0"
        for i in range(len(num1)):
            digit = int(num1[-(i+1)])
            multWithOther = self.multWithSingle(num2, digit)
            if multWithOther != "0":
                multWithOther = multWithOther + "0"*i
            total = self.sum(total, multWithOther)
        return str(total)

s = Solution()
res = s.multiply('9111', '0')
# res = s.sum('99', '1')
# res = s.multWithSingle('9111', 0)
print(res)