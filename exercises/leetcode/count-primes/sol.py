import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        primes = [False, False] + [True] * (n - 2)
        
        for x in range(2, int(math.sqrt(n)) + 1):
            if not primes[x]:
                continue

            for mult in range(x * x, n, x):
                primes[mult] = False

        return sum(primes)
    