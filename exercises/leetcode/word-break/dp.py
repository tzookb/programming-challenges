from typing import Counter, List, Optional

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # print(i + len(word), len(s))
                if i + len(word) > len(s):
                    continue
                if s[i: i + len(word)] != word:
                    continue
                dp[i] = dp[i + len(word)]

                if dp[i]:
                    break
        
        return dp[0]




s = "leetcode"
wordDict = ["leet","code"]
sol = Solution()
res = sol.wordBreak(s, wordDict)
print(res)
