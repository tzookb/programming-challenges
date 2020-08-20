from typing import List

from typing import List

class Solution:
    def __init__(self):
        self.memo = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in self.memo:
            return self.memo[s]

        if s == "":
            self.memo[s] = True
            return True
        for i in range(len(s)):
            part = s[0:i+1]
            if part not in wordDict:
                continue
            rest = s[i+1:]
            partRes = self.wordBreak(rest, wordDict)
            print(part, rest, partRes)
            if partRes:
                self.memo[s] = True
                return True
        self.memo[s] = False
        return False

s = "catsandog"
wordDict = ["cats", "dog", "sand", "an", "cat"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
