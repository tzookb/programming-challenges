from ctypes import pointer
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = self.buildGraphs(words)
        rules = self.getRules(words)
        letters = self.getLetters(words)

        for pointer, pointee in rules:
            letters[pointee] += 1
        


    
        for lt in letters:
            if lt in pointed_on_graph:
                continue
            pointed_on_graph[lt] = {}

        final = []
        count = 0
        while len(final) < len(letters):
        # while count < 7:
            not_pointed_on = []
            # find the not pointed on items
            for lt in pointed_on_graph:
                if pointed_on_graph[lt]:
                    continue
                not_pointed_on.append(lt)
            # remove their points
            for lt in not_pointed_on:
                del pointed_on_graph[lt]
                for k in pointed_on_graph:
                    if lt in pointed_on_graph[k]:
                        del pointed_on_graph[k][lt]

            final += not_pointed_on
            count += 1

        return "".join(final)

    def getLetters(self, words: List[str]):
        letters = {}
        for word in words:
            for c in word:
                letters[c] = 0
        return letters

    def buildGraphs(self, words: List[str]):
        point_to_graph = {}
        rules = self.getRules(words)
        for depender, dependee in rules:
            if depender not in point_to_graph:
                point_to_graph[depender] = {}
            point_to_graph[depender][dependee] = True

        return point_to_graph

    def getRules(self, words: List[str]):
        rules = []
        for i in range(len(words) - 1):
            cur = words[i]
            next = words[i + 1]
            rule = self.getRule(cur, next)
            if rule:
                rules.append(rule)
        return rules

    def getRule(self, w1, w2):
        for c1, c2 in zip(w1, w2):
            if c1 == c2:
                continue
            return [c1, c2]
        return None

inp = [
    "wrt",
    "wrf",
    "er",
    "ett",
    "rftt"
]
sol = Solution()
res = sol.alienOrder(inp)
print(res)
