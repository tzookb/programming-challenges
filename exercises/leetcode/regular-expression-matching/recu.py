class Solution:
    def getNextReg(self, p: str) -> (str, str, str):
        if p is "":
            return "", "0", ""
        if len(p) == 1:
            return p, "1", ""
        char = p[-2]
        count = p[-1]
        if count in ["+", "*"]:
            left = p[0:-2]
        else:
            left = p[0:-1]
            count = "1"
            char = p[-1]
        
        return char, count, left

    def partValidate(self, s: str, c: str, count: str) -> str:
        if count == "1":
            if s == "":
                raise NameError('HiThere a')
            if s[-1] != c and c != ".":
                raise NameError('HiThere')
            return s[0:-1]

        if count == "*":
            if s == "":
                return ""
            if s[-1] != c and c != ".":
                return s

        i = len(s) - 1
        count = 0
        while i >= 0:
            cur = s[i]
            if cur == c or c == ".":
                count += 1
                i -= 1
            else:
                break
        return s[0:-count]

    def isMatch(self, s: str, p: str) -> bool:
        reg = p
        leftS = s[::]
        while reg:
            char, count, reg = self.getNextReg(reg)
            try:
                print(char, count, reg, leftS)
                leftS = self.partValidate(leftS, char, count)
                print(leftS)
                print("-------")
            except NameError as e:
                print('errrr', e)
                return False
        
        return False if leftS or reg else True


s = Solution()
res = s.isMatch('aab', 'c*a*b*')
print(res)

# x = "abcdef"
# print(x[0:-1])