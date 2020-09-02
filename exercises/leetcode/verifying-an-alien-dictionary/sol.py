from typing import List

class Solution:

    def checkWordsPair(self, word1: str, word2: str) -> bool:
        for c1, c2 in zip(word1, word2):
            c1Val = self.charOrder[c1]
            c2Val = self.charOrder[c2]
            print(c1, c1Val, c2, c2Val)
            if c1Val < c2Val:
                return True
            if c1Val > c2Val:
                return False
        return len(word1) < len(word2)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.charOrder = {c: i + 1 for i, c in enumerate(order)}

        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            if not self.checkWordsPair(word1, word2):
                return False
        return True


words = ["hello","leetcode"]
order = "hlabcdefgijkmnopqrstuvwxyz"
s = Solution()
res = s.isAlienSorted(words, order)
print(res)