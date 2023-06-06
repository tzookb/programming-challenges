class Solution:
    def minimumCost(self, s: str) -> int:
        changes = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                changes += min(i, len(s) - i)
        return changes
            