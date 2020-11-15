from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        res = self.wordBreakBack(s, wordDict)
        return list(map(lambda x: " ".join(x), res))

    def wordBreakBack(self, s: str, wordDict: List[str]) -> List[str]:
        if s == "":
            return [[]]
        if s in self.memo:
            return self.memo[s]

        results = []
        for word in wordDict:
            if not s.startswith(word):
                continue
            left = s[len(word):]
            paths = self.wordBreakBack(left, wordDict)
            for path in paths:
                results.append(
                    [word] + path
                )
        self.memo[s] = results
        return results



word = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
res = s.wordBreak(word, wordDict)
print(res)