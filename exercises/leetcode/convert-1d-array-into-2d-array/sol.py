class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) > m * n:
            return []
        if len(original) / m != n:
            return []
        
        final = [[0] * n for _ in range(m)]
        
        pos = 0

        for r in range(m):
            for c in range(n):
                final[r][c] = original[pos]
                pos += 1

        return final