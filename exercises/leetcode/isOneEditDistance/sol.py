class Solution:
    def solveSameLen(self, word1: str, word2: str) -> int:
        foundDiff = False
        for c1, c2 in zip(word1, word2):
            if c1 != c2 and foundDiff:
                return False
            if c1 != c2 and not foundDiff:
                foundDiff = True
        return foundDiff
                

    def solveDiffLen(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            longer = word1
            shorter = word2
        else:
            longer = word2
            shorter = word1

        i = 0
        while i < len(shorter):
            if longer[i] != shorter[i]:
                break
            i += 1

        # ab 
        # acb
        restLong = longer[i+1:]
        restShort = shorter[i:]
        print(restLong, restShort)
        return restLong == restShort


    def isOneEditDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        diff = abs(l1 - l2)
        if diff == 0:
            return self.solveSameLen(word1, word2)
        elif diff == 1:
            return self.solveDiffLen(word1, word2)
        else:
            return False

s = Solution()
x = "abcd"
res = s.isOneEditDistance("", "")
print(res)
# print(x[1:])