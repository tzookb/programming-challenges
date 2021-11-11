from typing import List

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        dists = [[float("inf"), float("inf"), float("inf")] for i in range(len(colors) + 2)]

        for i in range(1, len(dists) -1):
            cur_color = colors[i - 1]
            index_to_zerofy = cur_color - 1
            dists[i][index_to_zerofy] = 0

            dists[i][0] = min(dists[i][0], dists[i - 1][0] + 1)
            dists[i][1] = min(dists[i][1], dists[i - 1][1] + 1)
            dists[i][2] = min(dists[i][2], dists[i - 1][2] + 1)

        for i in range(len(dists) - 2, 0, -1):
            cur_color = colors[i - 1]
            index_to_zerofy = cur_color - 1
            dists[i][index_to_zerofy] = 0

            dists[i][0] = min(dists[i][0], dists[i + 1][0] + 1)
            dists[i][1] = min(dists[i][1], dists[i + 1][1] + 1)
            dists[i][2] = min(dists[i][2], dists[i + 1][2] + 1)

        dists.pop(0)
        dists.pop()

        results = []
        for query in queries:
            idx = query[0]
            val = query[1]
            dist = dists[idx][val-1] if dists[idx][val-1] != float("inf") else -1
            results.append(dist)

        return results

# colors = [1,1,2,1,3,2,2,3,3]
# queries = [[1,3],[2,2],[6,1]]

colors = [1,2]
queries = [[0,3]]

s = Solution()
res = s.shortestDistanceColor(colors, queries)
print(res)
