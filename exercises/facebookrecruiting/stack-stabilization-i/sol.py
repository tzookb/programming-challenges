from typing import List

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
    if N == 0:
        return 0

    changes = 0
    prev = R[-1]
    for i in range(N - 2, -1, -1):
        cur = R[i]
        if cur >= prev:
            changes += 1
            prev = prev - 1
        else:
            prev = cur
        if prev < 1:
            return -1
    
    return changes

N = 5
R = [2, 5, 3, 6, 5]
# 3

N = 3
R = [100, 100, 100]
# 2

N = 4
R = [6, 5, 4, 3]
# -1

res = getMinimumDeflatedDiscCount(N, R)
print(res)
