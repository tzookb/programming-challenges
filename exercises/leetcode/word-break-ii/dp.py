from typing import List
from collections import Counter

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        if set(Counter(s).keys()) > set(Counter("".join(wordDict)).keys()):
            return []
            
        dp = [[]] * (len(s) + 1)
        dp[0] = [[""]]
        words = set(wordDict)
        
        for end in range(1, len(s)+1):
            curDp = []
            for start in range(0, end):
                cur = s[start:end]
                if cur not in words:
                    continue
                prevSols = dp[start]
                
                for sol in prevSols:
                    temp = sol + [cur]
                    curDp.append(temp)
            dp[end] = curDp
        
        return list(map(lambda x: " ".join(x).strip(), dp[-1]))

word = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
s = Solution()
res = s.wordBreak(word, wordDict)
print(res)