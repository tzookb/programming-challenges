from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp = [float("inf")] * (len(s) + 1)
        dp[0] = 0

        for i in range(len(s)):
            dpidx = i + 1

            for w in dictionary:
                minRemoval = dp[dpidx - 1] + 1
                if i - len(w) + 1 < 0:
                    continue
                prevWord = s[i - len(w) + 1: i + 1]
                if w != prevWord:
                    continue

                curRemoval = dp[dpidx - len(w)]
                
                minRemoval = min(minRemoval, curRemoval)

                dp[dpidx] = minRemoval
        
        print(dp)
        return dp[-1]

s = Solution()
res = s.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])
# res = s.minExtraChar(s = "dwmodizxvvbosxxw", dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"])
print(res)