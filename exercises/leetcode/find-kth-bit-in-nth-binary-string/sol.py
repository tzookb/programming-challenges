class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        cur = [0]
        for _ in range(n - 1):
            flipped = [0 if x == 1 else 1 for x in cur][::-1]
            cur = cur + [1] + flipped
        
        return str(cur[k - 1])
    