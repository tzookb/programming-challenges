from ctypes import pointer
from typing import List

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            if len(w1) <= len(w2):
                continue
            if w1.startswith(w2):
                return ""

        graph = self.buildGraphs(words)
        in_degree = self.getInDegree(graph, words)

        queue = []
        for k in in_degree:
            if in_degree[k] > 0:
                continue
            queue.append(k)

        final = []

        while queue:
            cur = queue.pop(0)
            final.append(cur)
            if cur not in graph:
                continue
            points_on = graph[cur]
            for pointed_on in points_on:
                in_degree[pointed_on] -= 1
                if in_degree[pointed_on] == 0:
                    queue.append(pointed_on)
        
        all_letters = self.getLetters(words)
        if len(final) < len(all_letters):
            return ""

        return "".join(final)

    def getInDegree(self, graph, words):
        in_degree = {}
        letters = self.getLetters(words)
        for letter in letters:
            in_degree[letter] = 0
            
        for node in graph:
            for pointed_on in graph[node]:
                in_degree[pointed_on] += 1

        return in_degree

    def getLetters(self, words: List[str]):
        letters = set()
        for word in words:
            for c in word:
                letters.add(c)
        return letters

    def buildGraphs(self, words: List[str]):
        graph = {}
        
        rules = self.getRules(words)
        for depender, dependee in rules:

            if depender not in graph:
                graph[depender] = {}
            graph[depender][dependee] = True

        return graph

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

# words = ["wrt","wrf","er","ett","rftt"] #wertf
# words = ["z","x"] #zx
# words = ["z","x","z"] #
# words = ["abc", "ab"] # 
# words = ["z", "z"] # z
words = ["abc", "z", "ad"] # 
s = Solution()
res = s.alienOrder(words)
print(res)