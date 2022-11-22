from typing import List, Counter
import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 2

        primes = [False, False] + [True] * (n - 2)
        print(primes)
        
        for x in range(2, int(math.sqrt(n)) + 1):
            mult = x * x
            while mult < n:
                primes[mult] = False
                mult += x

        return sum(primes)

s = Solution()
sol = s.countPrimes(10)
print(sol)