from typing import List
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        calc = []
        size = len(mat) * len(mat[0])
        visited = {}
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 0:
                    calc.append((r, c, 0))

        while calc:
            r, c, closest = calc.pop(0)
            key = f"{r}-{c}"
            if r < 0 or r >= len(mat):
                continue
            if c < 0 or c >= len(mat[0]):
                continue
            if key in visited:
                continue
            visited[key] = True
            mat[r][c] = closest
            calc.append((r + 1, c, closest + 1))
            calc.append((r - 1, c, closest + 1))
            calc.append((r, c + 1, closest + 1))
            calc.append((r, c - 1, closest + 1))

        return mat

s = Solution()
mat = [[0,0,0],[0,1,0],[0,0,0]]
res = s.updateMatrix(mat)
print(res)