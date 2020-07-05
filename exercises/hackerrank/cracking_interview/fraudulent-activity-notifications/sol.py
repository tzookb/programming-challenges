import math
import statistics
import bisect
from heapq import heappop, heappush, heapify

class MaxMinHeap:
    def __init__(self, type):
        self.arr = []
        self.type = type
    def push(self, item):
        heappush(self.arr, item)
    def push(self, item):
        heappush(self.arr, item)
    

maxHeap = []
minHeap = []


def activityNotifications(expenditure, d):
    notifications = 0
    totalDays = len(expenditure)
    pastExpenditure = expenditure[0:d]
    sa = []
    for item in pastExpenditure:
        heappush(sa, item)
    
    for i in range(d, totalDays):
        cur = expenditure[i]
        median = statistics.median(sa)
        if cur >= median*2:
            notifications += 1
        
        toRemove = expenditure[i-d]
        sa.remove(toRemove)
        sa.add(cur)
    return notifications


expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
d = 5
res = activityNotifications(expenditure, d)
print(res)
# print(getPalindromCount('aaabaa', 3))
