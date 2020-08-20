from typing import List

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        openers = [-1]
        maxLen = 0

        for idx in range(len(s)):
            print(openers)
            c = s[idx]
            if c == "(":
                openers.append(idx)
                continue
            else:
                if openers:
                    openers.pop()
                if openers:
                    curLen = idx - openers[-1]
                    maxLen = max(maxLen, curLen)
                else:
                    openers.append(idx)
        return maxLen


# (()) 4
# ))(() 2
# )())(()) 4
sol = Solution()
res = sol.longestValidParentheses("()(()")
print(res)
