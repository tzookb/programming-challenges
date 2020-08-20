class Solution:
    def minOperations(self, n: int) -> int:
        total = 0
        for i in range(n):
            total += (2 * i) + 1

        per = int(total / n)
        steps = 0
        for i in range(n):
            cur = (2 * i) + 1
            if cur > per:
                break
            steps += per - cur

        return steps
