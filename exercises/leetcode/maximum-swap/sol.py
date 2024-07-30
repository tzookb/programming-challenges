from typing import List, Counter, Optional
from heapq import heappush, heappop, heapify
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num

        str_num = list(str(num))

        digits = [[] for _ in range(10)]
        
        for i in range(len(str_num)):
            cur = int(str_num[i])
            digits[cur].append(i)
            
        for i in range(len(str_num)):
            cur = str_num[i]            
            if cur == "9":
                continue

            for j in range(9, int(cur), -1):
                if not digits[j]:
                    continue
                
                smallestidx = digits[j][-1]
                if smallestidx < i:
                    continue
                str_num[i], str_num[smallestidx] = str_num[smallestidx], str_num[i]
                
                return int("".join(str_num))

        return num

s = Solution()
res = s.maximumSwap(2736)

print(res)
