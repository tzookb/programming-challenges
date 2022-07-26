from typing import List, Optional

operatos = "+-*/"
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        items = []
        for token in tokens:
            if token not in operatos:
                items.append(int(token))
                continue
            right = items.pop()
            left = items.pop()
            print(left, token, right)
            if token == "+":
                result = left + right
            elif token == "/":
                result = int(left/right)
            elif token == "*":
                result = left * right
            elif token == "-":
                result = left - right
            
            items.append(result)
        
        return items[-1]

# data = ["4","13","5","/","+"]
# data = ["2","1","+","3","*"]
data = ["1","1","1","1","+","+","-"]
s = Solution()
res = s.evalRPN(data)
print(res)
# print(6//-132)
# print(int("-11"))