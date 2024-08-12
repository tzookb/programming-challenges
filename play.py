from typing import List, Dict, Counter
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        pass

    def isPrime(self, n: int) -> bool:
        if n <= 2:
            return True
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

s = Solution()
res = s.getFactors(12)
print(res)

