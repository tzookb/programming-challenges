from typing import List

def removeDupStars(pattern):
    cleaned = [-1]
    for c in pattern:
        prev = cleaned[-1]
        if c == "*" and prev == "*":
            continue
        cleaned.append(c)
    
    return "".join(cleaned[1:])
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def recu(word, pattern):
            key = (word, pattern)
            if key in memo:
                return memo[key]
            if word == pattern or pattern == "*":
                memo[key] = True
            elif not word or not pattern:
                memo[key] = False
            elif word[0] == pattern[0] or pattern[0] == "?":
                memo[key] = recu(word[1:], pattern[1:])
            elif pattern[0] == "*":
                memo[key] = recu(word, pattern[1:]) or recu(word[1:], pattern)
            else:
                memo[key] = False
            
            return memo[key]

        return recu(s, removeDupStars(p))

x = "a"
y = "*"
s = Solution()
res = s.isMatch(x, y)
print(res)