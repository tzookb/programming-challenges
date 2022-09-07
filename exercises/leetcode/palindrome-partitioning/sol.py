from typing import List
class Solution:
    def isPalindrom(self, s: str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        result = []
        def backtrack(cur, leftover):
            if not leftover:
                result.append(cur.copy())
            for i in range(len(leftover)):
                word = leftover[0:i+1]
                left = leftover[i+1:]

                if not self.isPalindrom(word):
                    continue

                cur.append(word)
                backtrack(cur, left)
                cur.pop()
        
        backtrack([], s)
        return result


test = "abbac"
# test = "aab"
# test = "efe"
s = Solution()
res = s.partition(test)
print(res)