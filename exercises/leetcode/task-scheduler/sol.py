import collections
from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = collections.Counter()
        for t in tasks:
            counters[t] += 1

        heap = []
        # heapify(heap)
        for cnt in counters:
            heappush(heap, -counters[cnt])
        
        waitStack = [None] * (n+1)

        count = 0

        while heap or waitStack:

            if waitStack:
                poppedVal = waitStack.pop(0)
                if poppedVal:
                    heappush(heap, -poppedVal)

            if heap:
                count += 1
                popped = -1 * heappop(heap)
                popped -= 1
                if popped > 0:
                    waitStack.append(popped)
            
        print(count)

        
s = Solution()
res = s.leastInterval(["A","A","A","B","B","B"], 2)
# res = s.connect_numbers("42/3")
print(res)

# abcabcabc__c__c__c
# a