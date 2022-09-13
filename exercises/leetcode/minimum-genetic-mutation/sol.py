from typing import Counter, Dict, List

class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1

        graph = self._buildGraph([start] + bank)

        visited = {}
        bfs = [(start, 0)]
        while bfs:
            cur, dist = bfs.pop(0)
            if cur == end:
                return dist
            if cur in visited:
                continue
            visited[cur] = True
            if cur not in graph:
                continue
            for neighbour in graph[cur]:
                bfs.append((neighbour, dist + 1))
        
        return -1


    def _buildGraph(self, bank: List[str]) -> Dict[str, Dict[str, bool]]:
        graph = {}
        for idx, word in enumerate(bank):
            for j in range(idx + 1, len(bank)):
                next_word = bank[j]
                if not self._isOneCharDiff(word, next_word):
                    continue
                if word not in graph:
                    graph[word] = {}
                if next_word not in graph:
                    graph[next_word] = {}
                
                graph[word][next_word] = True
                graph[next_word][word] = True
        return graph

    def _isOneCharDiff(self, w1: str, w2: str) -> bool:
        diffed = False
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if diffed:
                    return False
                diffed = True
        return True

start = "AAAAACCC"
end = "AACCCCCC"
bank = ["AAAACCCC","AAACCCCC","AACCCCCC"]

s = Solution()
res = s.minMutation(start, end, bank)
print(res)