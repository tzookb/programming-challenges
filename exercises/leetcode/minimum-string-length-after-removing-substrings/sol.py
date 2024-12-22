class Solution:
    def minLength(self, s: str) -> int:
        sol = ["#"]
        for c in s:
            if c == "D" and sol[-1] == "C":
                sol.pop()
                continue
            elif c == "B" and sol[-1] == "A":
                sol.pop()
                continue
            sol.append(c)
        
        return len(sol) - 1
        