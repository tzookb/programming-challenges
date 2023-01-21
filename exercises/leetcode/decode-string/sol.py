from typing import List, Optional
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
                continue

            parts = []
            while stack[-1] != "[":
                parts.append(stack.pop())
            parts = parts[::-1]
            
            stack.pop() #remove [

            mult = []
            while stack and stack[-1].isdigit():
                mult.append(stack.pop())
            mult = int("".join(mult[::-1]))
            build = ("".join(parts)) * int(mult)
            stack.append(build)
        
        return "".join(stack)


# word = "3[a]2[bc]"
# Output: "aaabcbc"
word = "3[a2[c]]"
# Output: "accaccacc"
s = Solution()
res = s.decodeString(word)
print(res)
