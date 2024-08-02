from typing import List, Counter, Optional
from collections import deque
from heapq import heappush, heappop, heapify

def getMissing(arr: list[int]) -> str:
    final = []
    if not arr:
        return "0-99"
    
    
    arr = [-1] + arr + [100]
    
    for i in range(1, len(arr)):
        cur = arr[i]
        prev = arr[i - 1]
        diff = cur - prev
        if diff == 1:
            continue

        if diff == 2:
            final.append(str(prev + 1))
        elif diff == 3:
            final.append(str(prev + 1))
            final.append(str(prev + 2))
        else:
            final.append( str(prev + 1) + "-" + str(cur - 1))

    return ",".join(final)

res = getMissing([3, 10, 98])
print(res)