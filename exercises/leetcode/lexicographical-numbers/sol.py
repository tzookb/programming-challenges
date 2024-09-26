class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        bfs = []
        sol = []

        for i in range(9, 0, -1):
            bfs.append(i)

        while bfs:
            cur = bfs.pop()
            if cur > n:
                continue
            sol.append(cur)
            mult = cur * 10
            for i in range(9, -1, -1):
                bfs.append(mult + i)
        return sol