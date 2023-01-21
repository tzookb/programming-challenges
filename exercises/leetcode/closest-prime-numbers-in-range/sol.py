from typing import List
import math
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        prev = math.inf
        diff = math.inf
        pair = [-1, -1]

        for cur in range(left, right + 1):
            if not self.__is_prime(cur):
                continue
            cur_diff = abs(cur - prev)
            if cur_diff < diff:
                diff = cur_diff
                pair = [prev, cur]
                if diff <= 2:
                    return pair

            prev = cur
        
        return pair

    def __is_prime(self, num: int) -> bool:
        if num < 2:
            return False
        if num <= 3:
            return True
        if num % 2 == 0:
            return False
        if num % 3 == 0:
            return False
        for i in range(5, int(math.sqrt(num)) + 1, 2):
            if num % i == 0:
                return False
        return True
