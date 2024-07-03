from typing import List

def getSecondsRequired(N: int, F: int, P: List[int]) -> int:
    P.sort()
    hops = 0
    for i in range(1, F):
        prev = P[i - 1]
        cur = P[i]
        diff = cur - prev
        if diff > 1:
            hops += diff - 1

    hops += N - 1 - P[-1]
    hops += F

    return hops