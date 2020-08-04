import collections

class StrCnt:
    def __init__(self, theStr):
        self.chars = collections.Counter(theStr)
        self.added = collections.Counter()

    def add(self, char):
        self.added[char] += 1

    def remove(self, char):
        if self.added[char] == 1:
            del self.added[char]
            return
        self.added[char] -= 1

    def isValid(self):
        for char in self.chars:
            if not self.added[char]:
                return False
            if self.added[char] < self.chars[char]:
                return False
        return True

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        desired = StrCnt(t)
        sx = 0
        ex = 0
        whoMoved = 0
        minStr = ''
        minStrSize = float('inf')

        while sx <= ex:
            isValid = desired.isValid()
            if isValid:
                curValidStr = s[sx:ex]
                if len(curValidStr) < minStrSize:
                    minStrSize = len(curValidStr)
                    minStr = curValidStr
                # print(desired.added)
                desired.remove(s[sx])
                sx += 1
            else:
                if ex >= len(s):
                    break
                desired.add(s[ex])
                ex += 1

        return minStr
        

n = [2,3,2]
s = Solution()
# res = s.minWindow("ADOBECODEBANC", "ABC")
# res = s.minWindow("ABCBA", "AB")
a = 1,2,3
print(a[0])
# print(len(collections.Counter("AAAABBC")))
# print(res)
# print(n[1:])