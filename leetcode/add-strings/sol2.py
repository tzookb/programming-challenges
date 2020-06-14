class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res1, res2= 0, 0
        for d in num1:
            res1= res1*10 + (ord(d)- ord('0'))
        for d in num2:
            res2= res2*10 + (ord(d)- ord('0'))
        return str(res1+ res2)

    # 0 == 48

s = Solution()
print(s.addStrings("1", "9"))
# print(s.addStrings("12", "34") == "46")

