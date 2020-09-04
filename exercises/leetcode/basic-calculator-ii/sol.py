class Solution:
    def action(self, a, b, op):
        if op == "*":
            return a * b
        elif op == "/":
            sign = 1 if a > 0 and b > 0 else -1
            return sign * (abs(a) // abs(b))

    def correct_numbers(self, arr):
        numbersArr = []
        curNum = 0
        for char in arr:
            if char.isdigit():
                curNum = curNum*10 + int(char)
            else:
                numbersArr.append(curNum)
                numbersArr.append(char)
                curNum = 0
        numbersArr.append(curNum)
        return numbersArr

    def isStrongOper(self, c: str) -> bool:
        return c in {"*": True, "/": True}

    def calculate(self, s: str) -> int:
        onlySimple = []
        s = s.replace(" ", "")
        arr = self.correct_numbers(s)
        stack = [arr.pop(0)]

        for i in range(1, len(arr), 2):
            oper = arr[i-1]
            val = arr[i]
            if self.isStrongOper(oper):
                prev = stack.pop()
                stack.append(
                    self.action(prev, val, oper)
                )
            else:
                sign = 1 if oper == "+" else -1
                stack.append(sign * val)

        return sum(stack)

        
s = Solution()
res = s.calculate("14-3/2")
# res = s.connect_numbers("42/3")
print(res)