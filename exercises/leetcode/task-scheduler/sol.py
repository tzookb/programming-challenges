import collections
from typing import List
from heapq import heapify, heappop, heappush

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counters = [0] * 26
        for t in tasks:
            counters[ord(t) - ord("A")] += 1
        counters.sort(reverse=True)

        tasks_count = 0
        idles = 0

        for count in counters:
            if count == 0:
                break
            tasks_count += count
            min_idles = (count - 1) * n
            print(min_idles)
            total_min_time = min_idles + count
            if total_min_time < idles:
                idles -= count
        
        print(tasks_count + idles)
        


s = Solution()
res = s.leastInterval(["A","A","A","B","B","B"], 2)
# res = s.connect_numbers("42/3")
print(res)

# abcabcabc__c__c__c
# a