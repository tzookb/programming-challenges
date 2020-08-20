from typing import List

class Solution:
    def numDecodings(self, s: str) -> int:
        tillHere = [1]
        val = 1 if 9 >= int(s[0]) >= 1 else 0
        tillHere.append(val)

        for idx in range(1, len(s)):
            curWays = 0
            oneDigVal = int(s[idx])
            twoDigVal = int(s[idx-1:idx+1])

            if 9 >= oneDigVal >= 1:
                curWays += tillHere[idx]
            if 26 >= twoDigVal >= 10:
                curWays += tillHere[idx-1]
            tillHere.append(curWays)

        return tillHere[-1]
        
s = Solution()
res = s.numDecodings("226")
print(res)
