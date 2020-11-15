from typing import List

class Solution:

    def __init__(self):
        self.memo = {}

    def canBuild(self, word, mapped, is_main) -> bool:
        if word in self.memo:
            return self.memo[word]
        if word == "" and not is_main:
            return True
        if not is_main and word in mapped:
            return True
    
        for i in range(1, len(word)):
            prefix = word[0:i]
            left = word[i:]
            if prefix not in mapped:
                continue
            if self.canBuild(left, mapped, False):
                self.memo[word] = True
                return True
        self.memo[word] = False
        return False

    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        found = []
        mapped = set(words)
        words = sorted(words, key=len, reverse=True)

        for word in words:
            if self.canBuild(word, mapped, True):
                found.append(word)

        return found

s = "catsandog"
# wordDict = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
wordDict = ["catdog","cat","dog"]
# wordDict = [""]
sol = Solution()
res = sol.findAllConcatenatedWordsInADict(wordDict)
print(res)
