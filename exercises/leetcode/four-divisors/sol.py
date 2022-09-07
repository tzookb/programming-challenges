import math
from typing import Counter, List, Optional

class Solution:
    def getDivisors(self, num: int) -> List[int]:
        sqrted = math.floor(math.sqrt(num))
        divisors = set()
        for leftd in range(1, sqrted + 1):
            if num % leftd > 0:
                continue
            rightd = num // leftd
            divisors.add(leftd)
            divisors.add(rightd)
        return list(divisors)

    def sumFourDivisors(self, nums: List[int]) -> int:
        cached = {}
        total = 0
        for num in nums:
            if num in cached:
                total += cached[num]
                continue
            divisors = self.getDivisors(num)

            sumval = 0
            if len(divisors) == 4:
                sumval = sum(divisors)
            cached[num] = sumval
            total += sumval
        return total
        

s = Solution()
# res = s.sumFourDivisors([21,4,7])
# res = s.sumFourDivisors([21,21])
res = s.sumFourDivisors([1,2,3,4,5,6,7,8,9,10])
# res = s.getDivisors(6)
print(res)