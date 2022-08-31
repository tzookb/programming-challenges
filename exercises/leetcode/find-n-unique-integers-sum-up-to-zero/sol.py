class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = []
        if n % 2 == 1:
            res.append(0)
        
        for step in range(n // 2):
            val = step + 1
            res.append(val)
            res.append(-val)

        return res
            
        