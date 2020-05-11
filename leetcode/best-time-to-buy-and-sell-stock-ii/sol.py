class Solution:

    def __init__(self):
        self.mappers = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in self.mappers:
                last_opener = stack.pop() if stack else '#'
                if self.mappers[char] != last_opener:
                    return False
            else:
                stack.append(char)
                continue

        return not stack

s = Solution()
r = s.isValid("[()][]")
print(r)