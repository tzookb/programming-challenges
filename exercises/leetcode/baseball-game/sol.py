from typing import List

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for item in ops:
            if item == "C":
                stack.pop()
            elif item == "D":
                stack.append(stack[-1] * 2)
            elif item == "+":
                stack.append(stack[-1] + stack[-2])
            else:
                stack.append(int(item))
        return sum(stack)
        

n = ["5","2","C","D","+"]
s = Solution()
res = s.calPoints(n)
print(res)
