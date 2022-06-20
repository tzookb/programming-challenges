class Solution:
    def nextGreaterElement(self, n: int) -> int:
        sList = list(str(n))
        i = len(sList) - 2
        while i >= 0 and sList[i] >= sList[i + 1]:
            i -= 1

        if i < 0:
            return -1

        j = len(sList) - 1
        while j >= 0 and sList[i] >= sList[j]:
            j -= 1

        sList[i], sList[j] = sList[j], sList[i]
        left = sList[0:i+1]
        right = sList[i+1:]
        resultList = left + right[::-1]
        resultStr = "".join(resultList)
        finalNumber = int(resultStr)

        if finalNumber > 2147483647:
            return -1
        
        return finalNumber
        

        
        