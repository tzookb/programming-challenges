class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.memo = {}
        res = self.wordBreakRec(s, wordDict)
        return list(map(lambda x: " ".join(x), res))
    
    def wordBreakRec(self, target, words):
        if target == "":
            return [[]]

        if target in self.memo:
            return self.memo[target]

        results = []
        for i in range(0 ,len(target)):
            first = target[0:i+1]
            sec = target[i+1:]
            if first in words:
                res = self.wordBreakRec(sec, words)
                if res:
                    for item in res:
                        results.append([first] + item)

        self.memo[target] = results
        return results
