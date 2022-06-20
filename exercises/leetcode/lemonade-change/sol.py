from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = [0, 0]
        
        for bill in bills:
            if bill == 5:
                register[0] += 1
            elif bill == 10:
                if register[0] < 1:
                    return False
                register[0] -= 1
                register[1] += 1
            else: #bill = 20
                if register[1] > 0 and register[0] > 0:
                    register[0] -= 1
                    register[1] -= 1
                elif register[0] > 2:
                    register[0] -= 3
                else:
                    return False

        return True

s = Solution()
res = s.lemonadeChange([5,5,5,20])
print(res)