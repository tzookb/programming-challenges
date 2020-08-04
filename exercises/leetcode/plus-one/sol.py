from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        addition = 1

        while i >= 0:
            cur = digits[i]
            cur += addition
            if cur > 9:
                cur = cur % 10
                addition = 1
            else:
                addition = 0

            digits[i] = cur
            i -= 1

        if addition:
            digits.insert(0, 1)

        return digits
