class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        added = 0
        openers = 0
        for c in s:
            if c == "(":
                openers += 1
            elif c == ")":
                if openers:
                    openers -= 1
                else:
                    added += 1
        
        added += openers

        return added
        