class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen = len(a)
        bLen = len(b)
        smallerLen = min(aLen, bLen)
        bigger = a if aLen > bLen else b

        finalStr = []

        remainder = 0
        for x in zip(a[::-1], b[::-1]):
            if x[0] == "1":
                remainder += 1
            if x[1] == "1":
                remainder += 1
            
            if remainder == 0:
                finalStr.insert(0, "0")
            elif remainder == 1:
                finalStr.insert(0, "1")
                remainder = 0
            elif remainder == 2:
                finalStr.insert(0, "0")
                remainder = 1
            elif remainder == 3:
                finalStr.insert(0, "1")
                remainder = 1

        # leftover
        for digit in bigger[::-1][smallerLen:]:
            if digit == "1":
                remainder += 1

            if remainder == 0:
                finalStr.insert(0, "0")
            elif remainder == 1:
                finalStr.insert(0, "1")
                remainder = 0
            elif remainder == 2:
                finalStr.insert(0, "0")
                remainder = 1
            elif remainder == 3:
                finalStr.insert(0, "1")
                remainder = 1
        
        if remainder:
            finalStr.insert(0, "1")

        return "".join(finalStr)

s = Solution()
res = s.addBinary('1111', '1111')
print(res)