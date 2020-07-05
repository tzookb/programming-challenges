import math
from typing import List
import collections

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        print(graph)
        return
        visited = [False] * len(times)
        nextStop = K
        while True:
            if visited[nextStop]:
                return False
            visited[nextStop] = True

times = [
    [2,1,1],
    [2,3,1],
    [3,4,1]
]
N = 4
K = 2
s = Solution()
res = s.networkDelayTime(times, N, K)