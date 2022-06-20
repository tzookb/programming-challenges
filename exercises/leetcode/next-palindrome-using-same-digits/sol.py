from typing import List

class Solution:
    def get_next_larger(self, sList):
        i = len(sList) - 2
        while i >= 0 and sList[i] >= sList[i + 1]:
            i -= 1

        if i < 0:
            return None

        j = len(sList) - 1
        while j >= 0 and sList[i] >= sList[j]:
            j -= 1

        sList[i], sList[j] = sList[j], sList[i]
        left = sList[0:i+1]
        right = sList[i+1:]
        return left + right[::-1]

    
    def getMidStr(self, num: str) -> str:
        mid = len(num) // 2
        midStr = "" if (len(num) % 2 == 0) else num[mid]
        return midStr
    
    def getLeftPart(self, num: str) -> str:
        mid = len(num) // 2
        return num[0:mid]

    def nextPalindrome(self, num: str) -> str:
        midStr = self.getMidStr(num)
        left_part = list(self.getLeftPart(num))
        
        next_larger = self.get_next_larger(left_part)

        if next_larger is None:
            return ""
        
        other_side = next_larger[::-1]
        together = next_larger + [midStr] + other_side

        return "".join(together)
