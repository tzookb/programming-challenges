from typing import Counter, List, Optional

class Solution:
    vouls = ['a', 'e', 'i', 'o', 'u']

    def getMatches(self, val = 0):
        matches = {}
        for v in self.vouls:
            matches[v] = val
        return matches

    def sumMatches(self, matches):
        summed = 0
        for key in matches:
            summed += matches[key]
        return summed % (10**9 + 7)

    def countVowelPermutation(self, n: int) -> int:
        count = 1
        matches = self.getMatches(1)

        while count < n:
            count += 1
            next_matches = self.getMatches(0)
            for key in matches:
                total = matches[key]
                if key == "a":
                    next_matches["e"] += total
                elif key == "e":
                    next_matches["a"] += total
                    next_matches["i"] += total
                elif key == "i":
                    next_matches["a"] += total
                    next_matches["e"] += total
                    next_matches["o"] += total
                    next_matches["u"] += total
                elif key == "o":
                    next_matches["i"] += total
                    next_matches["u"] += total
                elif key == "u":
                    next_matches["a"] += total
            matches = next_matches
        
        return self.sumMatches(matches)

s = Solution()
print(
    s.countVowelPermutation(144)
)