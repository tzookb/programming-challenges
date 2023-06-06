class Solution:
    def maxDepth(self, s: str) -> int:
        stack = 0
        deepest = 0

        for c in s:
            if c not in "()":
                continue
            if c == "(":
                stack += 1
                deepest = max(deepest, stack)
            else:
                stack -= 1