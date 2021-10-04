from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        sols = [""]

        for c in s:
            options = []
            if c.isalpha():
                options.append(c.lower())
                options.append(c.upper())
            else:
                options.append(c)
            
            next_sols = []
            for sol in sols:
                for option in options:
                    next_sols.append(sol + option)
            sols = next_sols
        
        return sols


s = Solution()
res = s.letterCasePermutation("3z4")
print(res)