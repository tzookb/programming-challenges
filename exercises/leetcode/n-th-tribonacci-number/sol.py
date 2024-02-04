class Solution:
    def tribonacci(self, n: int) -> int:
        steps = [0, 1, 1]
        if n <= 2:
            return steps[n]
        
        for _ in range(n - 2):
            summed = sum(steps)
            steps = [
                steps[1],
                steps[2],
                summed
            ]
        
        return steps[-1]