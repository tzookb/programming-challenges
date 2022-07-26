from typing import List

def getMinProblemCount(N: int, S: List[int]) -> int:
    max_val = max(S)
    has_odd = any(n % 2 == 1 for n in S)

    even_problems = max_val // 2
    odd_problems = max_val - even_problems * 2

    if has_odd and not odd_problems:
        even_problems -= 1
        odd_problems = 2
        
    return even_problems + odd_problems

N = 6
S = [1, 2, 3, 4, 5, 6]
# 4

N = 4
S = [4, 3, 3, 4]
# 3

N = 4
S = [2, 4, 6, 8]
# 4

res = getMinProblemCount(N, S)
print(res)
