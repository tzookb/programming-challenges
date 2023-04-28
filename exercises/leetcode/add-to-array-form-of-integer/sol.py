from typing import List
import itertools


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        k_list = [int(x) for x in str(k)]

        num = num[::-1]
        k_list = k_list[::-1]

        sol = []
        leftover = 0
        
        for a, b in list(itertools.zip_longest(num, k_list, fillvalue=0)):
            summed = a + b + leftover
            sol.append(summed % 10)
            leftover = summed // 10
        if leftover:
            sol.append(leftover)
        return sol[::-1]