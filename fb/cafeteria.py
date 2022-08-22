from typing import List

def getEnterInSpace(space, k):
    initial = k * 2 + 1
    if space < initial:
        return 0

    space -= initial
    extra_size = k + 1
    addional_spaces = space // extra_size

    return 1 + addional_spaces

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
    S.sort()
    S.insert(0, 0 - K)
    S.append(N + K + 1)
    total = 0

    for i in range(1, len(S)):  
        cur = S[i]
        prev = S[i - 1]
        diff = cur  - prev - 1
        enters = getEnterInSpace(diff, K)
        total += enters

    return total

N = 10
K = 1
M = 2
S = [2, 6]
res = getMaxAdditionalDinersCount(N, K, M, S)
print(res)
