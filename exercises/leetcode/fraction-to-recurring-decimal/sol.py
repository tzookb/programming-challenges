from typing import Counter, List

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        sign = "-" if numerator * denominator < 0 else ""
        numerator = abs(numerator)
        denominator = abs(denominator)
        intValue = numerator // denominator
        
        if intValue * denominator == numerator:
            return sign + str(intValue)

        floats = []
        remianders = {}

        left = numerator % denominator

        while left:
            if left in remianders:
                floats.insert(remianders[left], "(")
                floats.append(")")
                break
            remianders[left] = len(floats)
            left *= 10
            unit = left // denominator
            left = left % denominator
            floats.append(str(unit))

        final_num = str(intValue) + "." + "".join(floats)
        return sign + final_num
        
s = Solution()
res = s.fractionToDecimal(-214748, 1)
print(res)