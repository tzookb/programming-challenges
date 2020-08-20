from typing import List

class Solution(object):
    def multiply(self, num1, num2):
        res = 0
        iMult = 1
        for i in reversed(num1):
            jMult = 1
            for j in reversed(num2):
                res += iMult * (int(j)*int(i)) * jMult
                jMult *= 10
            iMult *= 10
        return res
        return str(res)

s = Solution()
res = s.multiply('10000000000000000000000000000000000000000', '9000000')
# res = s.sum('99', '1')
# res = s.multWithSingle('9', 9)
print(res)