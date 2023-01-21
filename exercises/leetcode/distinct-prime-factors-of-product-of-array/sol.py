from typing import List
import math

class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        arr = []
        for num in nums:
            cur = self.getPrimeFactors(num)
            arr += cur
        return len(list(set(arr)))

    def getPrimeFactors(self, num: int) -> List[int]:
        if self.isPrime(num):
            return [num]
        
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                break
        
        left = self.getPrimeFactors(i)
        right = self.getPrimeFactors(num // i)

        return list(set(left + right))

    def isPrime(self, num: int) -> bool:
        if num <= 1:
            return False
        
        for i in range(2, math.floor(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        
        return True

s = Solution()
# res = s.distinctPrimeFactors([2,4,3,7,10,6]) #4
res = s.distinctPrimeFactors([2,4,8,16]) #1
print(res)